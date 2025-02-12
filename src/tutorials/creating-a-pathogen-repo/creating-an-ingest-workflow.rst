===========================
Creating an ingest workflow
===========================

This tutorial dissects the `ingest workflow of the pathogen-repo-guide <https://github.com/nextstrain/pathogen-repo-guide/tree/main/ingest>`_
and the decisions needed to create an ingest workflow for a new pathogen.

.. note::

    You only need to create an ingest workflow if you do **not** want to use an existing pathogen ingest workflow maintained by Nextstrain.

.. contents:: Table of Contents
   :local:
   :depth: 2

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`.
2. Run through the :doc:`../using-a-pathogen-repo/running-an-ingest-workflow` tutorial. This will verify your installation and ensure that you are able to run an ingest workflow.

Additionally, to follow this tutorial, you will need:

* An understanding of `Snakemake <https://snakemake.readthedocs.io/en/stable/>`_ workflows.
* Pathogen-specific knowledge (e.g. WHO naming scheme) to help with decisions on how to set up the ingest workflow

Setup
=====

The Nextstrain `pathogen-repo-guide <https://github.com/nextstrain/pathogen-repo-guide>`_ can be used for setting up a
pathogen repository to hold the files necessary to run and maintain pathogen workflows.
This tutorial will only focus on using the guide to set up the ingest workflow.

1. Go to the Nextstrain `pathogen-repo-guide repository <https://github.com/nextstrain/pathogen-repo-guide>`_
2. Follow the `GitHub guide for creating a repository from a template <https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template>`_.
3. Follow the `GitHub guide to download the new repository <https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository>`_.
4. Change directory to your new pathogen repository

.. code-block:: console

    $ cd <new-pathogen-repository>

Decide on data source
=====================

The first step for creating an ingest workflow is to decide on the data source for your pathogen's data.
The pathogen-repo-guide only focuses on downloading public data from `NCBI <https://www.ncbi.nlm.nih.gov/>`_,
using the rules defined in ``ingest/rules/fetch_from_ncbi.smk``.

.. note::

    If your pathogen does not have sequences on NCBI, then you will need to explore other data sources that are not
    covered in this tutorial.

NCBI Datasets
-------------

By default, the pathogen-repo-guide is set to use the `NCBI Datasets CLI <https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/>`_
tool to download viral sequences using a provided `NCBI taxonomy <https://www.ncbi.nlm.nih.gov/taxonomy>`_ ID.
This is the simplest route for setting up an ingest workflow, but it is limited to a
`standard set of fields <https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/dataformat/tsv/dataformat_tsv_virus-genome/#fields>`_
that is parsed by NCBI Datasets.

You can decide whether NCBI Datasets include sufficient data for your pathogen by inspecting the uncurated data from NCBI Datasets CLI.

1. Add your pathogen's NCBI taxonomy ID to the ``ncbi_taxon_id`` parameter in the ``ingest/defaults/config.yaml`` config file.
2. Dump the uncurated metadata by running

.. code-block:: console

    $ nextstrain build ingest dump_ncbi_dataset_report

3. Inspect the generated file ``ingest/data/ncbi_dataset_report_raw.tsv``
4. If there are other fields in the raw file that you would like to include in the workflow,
   you can add them to the ``ncbi_datasets_fields`` parameter

If the data looks sufficient for your pathogen, then skip to the :ref:`curation-steps`.

NCBI Entrez
-----------

If your pathogen requires data from other fields not parsed by NCBI Datasets, then you will need to use
the `NCBI Entrez <https://www.ncbi.nlm.nih.gov/books/NBK25501/>`_ tool to download all available data in a GenBank file.

1. Add an Entrez search term to the ``entrez_search_term`` parameter in the ``ingest/defaults/config.yaml`` config file.

2. Create a custom script to parse the GenBank file into a flat `JSON Lines/NDJSON format <https://jsonlines.org/>`_.
   (We may provide an example script in the future, but this is currently not available.)

3. Edit the ``parse_genbank_to_ndjson`` rule in ``ingest/rules/fetch_from_ncbi.smk`` to use the custom script.

4. Switch the `Snakemake ruleorder <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#handling-ambiguous-rules>`_
   within the ``ingest/rules/fetch_from_ncbi.smk`` file.

.. code-block:: python

    ruleorder: format_ncbi_datasets_ndjson < parse_genbank_to_ndjson

4. Make sure the ``field_map`` parameters in the config file are using the field names of your custom NDJSON output.

.. _curation-steps:

Curation steps
==============

After the public data is downloaded, the next part of the workflow runs a pipeline of data curation commands and scripts
to format the metadata and sequences.

We highly encourage you to go through the commands used in the ``curate`` rule within ``ingest/rules/curate.smk``
to gain a deeper understanding of how they work.
We will give a brief overview of each step and their relevant config parameters defined in ``ingest/defaults/config.yaml`` to help you get started.

Rename fields
-------------

The :doc:`augur curate rename <augur:usage/cli/curate/rename>` command will rename the fields in the NDJSON records.

.. note::

    This is the first step of the pipeline so any subsequent references to field names should use the new field names.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.field_map``

    * A dictionary where the key is the original field name and value is the new field name

    * The default dictionary uses the original field names from NCBI Datasets and transforms them to the standard Nextstrain metadata fields.

Normalize strings
-----------------

The :doc:`augur curate normalize-strings <augur:usage/cli/curate/normalize-strings>` command will normalize string
values in the NDJSON records for predictable string comparisons.
Currently, there are no config parameters for this command.

Transform strain names
----------------------

The :doc:`augur curate transform-strain-name <augur:usage/cli/curate/transform-strain-name>` command will verify the
``strain`` field values match an expected pattern.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.strain_regex``

    * `Python regular expression <https://docs.python.org/3/howto/regex.html>`_ pattern the strain names must match

    * The default pattern (``^.+$``) accepts any non-empty string because we do not have a clear standard for strain names across pathogens

* ``curate.strain_backup_fields``

    * List of other NDJSON fields to use as strain name if the ``strain`` fails to match expected pattern

    * The default list uses the GenBank ``accession`` field as a stable back up field for messy strain fields.

Format dates
------------
The :doc:`augur curate format-dates <augur:usage/cli/curate/format-dates>` command will format date fields to
`ISO 8601 dates <https://en.wikipedia.org/wiki/ISO_8601>`_ (YYYY-MM-DD), where incomplete dates are masked with 'XX' (e.g. 2023 -> 2023-XX-XX).

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.date_fields``

    * List of NDJSON date fields to be formatted

    * The default list includes the standard date fields that are expected from NCBI records

* ``curate.expected_date_formats``

    * List of expected date formats in the provided date fields

    * The default list includes the date formats that are expected from NCBI records

Transform GenBank location
--------------------------

The :doc:`augur curate parse-genbank-location <augur:usage/cli/curate/parse-genbank-location>` command will try to parse locations in NDJSON records according to
`GenBank geo_loc_name qualifier <https://www.ncbi.nlm.nih.gov/genbank/collab/country/>`_.
It parses the ``location`` field into three fields:

* ``country``
* ``division``
* ``location``

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.genbank_location_field``

    * The NDJSON field that contains the GenBank ``geo_loc_name``.

Titlecase
---------

The :doc:`augur curate titlecase <augur:usage/cli/curate/titlecase>` command will make the first letter of every word
uppercase in provided string fields.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.titlecase.fields``

    * List of NDJSON fields to titlecase

    * The default list includes all of the geolocation fields from NCBI records (after running ``transform-genbank-location``)

* ``curate.titlecase.abbreviations``

    * List of strings to keep as all uppercase

    * The default list includes the country “USA” as an example

* ``curate.titlecase.articles``

    * List of strings to keep as all lowercase

    * The default list includes articles (e.g., 'and', 'the', 'of', etc) that we've encountered in past ingest pipelines

Abbreviate authors
------------------

The :doc:`augur curate abbreviate-authors <augur:usage/cli/curate/abbreviate-authors>` command will abbreviate the
authors list in the NDJSON records to ``<first author> et al.``.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.authors_field``

    * The NDJSON field that contains the authors list

    * The default value uses the field expected from NCBI records

* ``curate.authors_default_value``

    * The default string to use if the authors list is empty

    * The default value ``?`` will allow you to easily filter for records without authors.

* ``curate.abbr_authors_field``

    * The field name to use for the new abbreviated authors field.

    * If none are provided, the original authors field will be replaced with the abbreviated authors.

    * The default field is ``abbr_authors`` so you can compare the original and abbreviated author values.

Apply geolocation rules
-----------------------

The :doc:`augur curate apply-geolocation-rules <augur:usage/cli/curate/apply-geolocation-rules>` command will apply
geolocation standardizations across all records.
The command will use `Augur's built-in geolocation rules <https://github.com/nextstrain/augur/blob/@/augur/data/geolocation_rules.tsv>` by default.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.local_geolocation_rules``

    * A path to a local set of geolocation rules used to override the general rules

    * The default points to the empty file ``ingest/defaults/geolocation_rules.tsv`` where you can add your pathogen specific rules

Geolocation rules
~~~~~~~~~~~~~~~~~

Geolocation rules are defined in a TSV file with the format

.. code-block:: none

    region/country/division/location<\t>region/country/division/location

The first set of locations are the expected geolocations that are in the metadata and the second set of geolocations
after the tab are the standard geolocations that will be applied to the metadata.
Each geo resolution (region, country, division, location) is expected to be a field in the NDJSON.
By using the region/country/division/location hierarchy, we ensure that locations with the same name
(e.g., two  cities with the same name but in different countries) are treated differently based on their full hierarchy.
If there are rules that can be applied across multiple locations, then a wildcard (``*``) can be used instead of a specific value.

Let's say you have the following locations in your NDJSON

.. code-block:: none

    {“region”: “North America”, “country”: “United States”, “division”: “New York”, “location”: “Buffalo”}
    {“region”: “North America”, “country”: “United States”, “division”: “New York”, “location”: “New York”}

And you provide these geolocation rules

.. code-block:: none

    North America/United States/New York/New York		North America/United States/New York/New York City
    North America/United States/New York/*	North America/United States/New York State/*
    North America/United States/*/*	North America/USA/*/*

The first rule looks for the specific hierarchy to correct the location from “New York” to "New York City".
The second rule has a wildcard as the location, so it will correct all applicable divisions from “New York” to "New York State".
The third rule has wildcards for both division and location, so it will correct all applicable countries from “United States” to "USA".

Running through the :doc:`augur curate apply-geolocation-rules <augur:usage/cli/curate/apply-geolocation-rules>` command
should produce the following

.. code-block:: none

    {“region”: “North America”, “country”: “USA”, “division”: “New York State”, “location”: “Buffalo”}
    {“region”: “North America”, “country”: “USA”, “division”: “New York State”, “location”: “New York City”}

Apply record annotations
------------------------

The :doc:`augur curate apply-record-annotations <augur:usage/cli/curate/apply-record-annotations>` command merges user
curated annotations with the NDJSON records, with the user curations overwriting the existing fields.

As the final step in the curation pipeline, this command will output the NDJSON records as separate metadata TSV and
sequences FASTA files.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.annotations``

    * A path to a file of user annotations
    * The default points to the empty file ``ingest/defaults/annotations.tsv`` where you can add your pathogen-specific annotations

* ``curate.annotations_id``

    * The NDJSON field that has the ID used to match records to annotations
    * The default value uses the GenBank ``accession`` since they are guaranteed to be unique

* ``curate.output_id_field``

    * The NDJSON field to use as the sequence identifiers in the FASTA file
    * The default value uses the GenBank ``accession`` since they are guaranteed to be unique

* ``curate.output_sequence_field``

    * The NDJSON field that contains the genomic sequence
    * The default value uses ``sequence`` which is the field name we use for NCBI Datasets.

User annotations
~~~~~~~~~~~~~~~~

The user annotations are defined in a TSV file with the format

.. code-block:: none

    id<\t>field<\t>value

The ``id`` is used to match the NDJSON records.
The ``field`` is the field you are trying to overwrite or add to the NDJSON record.
The ``value`` is the value you are trying to add to the NDJSON record.

Let's say you have the following NDJSON records

.. code-block:: none

    {“accession”: “AAAAA”, “country”: “United States”, “division”: “New York”, “location”: “Buffalo”}
    {“accession”: “BBBBB”, “country”: “United States”, “division”: “New York”, “location”: “Buffalo”}

And you provide these user annotations

.. code-block:: none

    AAAAA	age	10
    BBBBB	age	12
    BBBBB	location	Niagara Falls

The first two annotations add the ``age`` field to the records and the
third annotation overwrites the existing ``location`` field for the record ``BBBBB``.

Running through the :doc:`augur curate apply-record-annotations <augur:usage/cli/curate/apply-record-annotations>` command
should produce the following:

.. code-block:: none

    {“accession”: “AAAAA”, “country”: “United States”, “division”: “New York”, “location”: “Buffalo”, “age”: 10}
    {“accession”: “BBBBB”, “country”: “United States”, “division”: “New York”, “location”: “Niagara Falls”, “age”: 12}

Subset metadata
---------------

Finally we use the `tsv-select <https://github.com/eBay/tsv-utils/blob/master/docs/tool_reference/tsv-select.md>`_ command
to subset the metadata to a list of metadata columns.

Config parameters
~~~~~~~~~~~~~~~~~

* ``curate.metadata_columns``

    * A list of metadata columns to include in the final output metadata TSV
    * The columns will be output in the order specified

Advanced usage
==============

The default ingest workflow of the pathogen-repo-guide is generalized to be able to work with any pathogen,
but this means you will need to tailor the ingest workflow for pathogen specific steps.

Add custom curation steps
-------------------------

The curation pipeline is designed to be extremely customizable, with each curation step reading NDJSON records
from stdin and outputing modified NDJSON records to stdout.
If you write a custom script that follows the same pattern, you can add your script as another step anywhere in the
curation pipeline before the final ``augur curate apply-record-annotations`` command.

A typical pathogen-specific step for curation is the standardization of strain names since pathogens usually have different naming conventions
(e.g. `influenza <https://www.cdc.gov/flu/about/viruses-types.html>`_ vs `measles <https://www.cdc.gov/measles/php/laboratories/genetic-analysis.html#cdc_generic_section_3-guidelines-for-naming-measles-strains-or-sequences>`_).
For example, we've added a step in the curation pipeline to normalize the strain names for the `Zika ingest workflow <https://github.com/nextstrain/zika/tree/main/ingest>`_.

1. We added a `custom Python script <https://github.com/nextstrain/zika/blob/a91e575bff38f154390c9eb11a44a89abf95a55b/ingest/bin/fix-zika-strain-names.py>`_
to the Zika repository which reads NDJSON records from stdin, edits the ``strain`` field per record, then outputs the modified records to stdout.

2. The script was `added to the curation pipeline <https://github.com/nextstrain/zika/blob/7b3fe1a27f0d013a8d51f6090718b7f617cc31a0/ingest/rules/curate.smk#L93-L94>`_
before the ``augur curate apply-record-annotations`` step to still allow user annotations to override the modified strain names if necessary.

Nextclade as part of ingest
---------------------------

Nextstrain is pushing to standardize our core ingest workflows to include :doc:`Nextclade <nextclade:user/nextclade-cli/index>` runs,
which allows us to merge clade/lineage designations and QC metrics with the metadata in our publicly hosted data.
However, this is not possible until you have already created a :doc:`Nextclade dataset <nextclade:user/datasets>` for your pathogen.

Here's our typical process for adding Nextclade to ingest workflows for new pathogens

1. Create an ingest workflow without Nextclade.
2. Run the ingest workflow to generate a set of curated metadata and sequences.
3. Use the curated metadata and sequences as input to generate a :doc:`reference tree <nextclade:user/input-files/04-reference-tree>`.
4. Create a Nextclade dataset by following the `Nextclade dataset creation guide <https://github.com/nextstrain/nextclade_data/blob/master/docs/dataset-creation-guide.md>`_.
5. Update the ingest workflow to run Nextclade using the new Nextclade dataset.

If your pathogen already has a Nextclade dataset, you can use the pathogen-repo-guide's ``ingest/defaults/nextclade_config.yaml``
config file to include the Nextclade rules from ``ingest/rules/nextclade.smk`` as part of the ingest workflow.

1. Add your Nextclade dataset name to the ``nextclade.dataset_name`` parameter
2. Run the ingest workflow with the additional config file

.. code-block:: bash

    nextstrain build ingest --configfile defaults/nextclade_config.yaml

Example ingest workflows
========================

Although we strive to keep Nextstrain core ingest workflows standardized, we cannot guarantee that every pathogen
ingest workflow will be kept up-to-date.

We recommend using the `zika ingest workflow <https://github.com/nextstrain/zika/tree/main/ingest>`_ and the
`mpox ingest workflow <https://github.com/nextstrain/mpox/tree/master/ingest>`_ as example workflows that
demonstrate our latest developments.

Next steps
==========

* Learn more about :doc:`augur curate commands <augur:usage/cli/curate/index>`
* We are planning to write another detailed tutorial for creating a phylogenetic workflow,
  but until that is ready you can follow the :doc:`simple phylogenetic workflow tutorial <../creating-a-phylogenetic-workflow>`.
