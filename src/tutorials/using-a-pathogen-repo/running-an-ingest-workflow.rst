==========================
Running an ingest workflow
==========================

This tutorial uses the :term:`Nextstrain CLI` to help you get started running :term:`ingest workflows<ingest workflow>`.
Ingest workflows download public data from NCBI and output :term:`ingest datasets <ingest dataset>`, which include curated
metadata and sequences that can be used as input for :term:`phylogenetic <phylogenetic workflow>` or :term:`Nextclade workflows <Nextclade workflow>`.

.. note::
  You only need to run an ingest workflow if you do not want to use the data files already publicly hosted by Nextstrain.
  Individual pathogen repositories include documentation that links to their data files.

In this tutorial, you will run the ingest workflow of our `Zika repository <https://github.com/nextstrain/zika>`_ and view outputs on your computer.
You will have a basic understanding of how to run ingest workflows for other pathogens and a foundation for understanding how to customize ingest workflows.

.. contents:: Table of Contents
   :local:

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`. These instructions will install all of the software you need to complete this tutorial.

Download the Zika repository
============================

All pathogen ingest workflows are stored in :term:`pathogen repositories<pathogen repository>` (version-controlled folders) to track changes over time.
Download the `Zika repository <https://github.com/nextstrain/zika>`_.

.. code-block::

    $ git clone https://github.com/nextstrain/zika
    Cloning into 'zika'...
    [...more output...]

When it's done, you'll have a new directory called ``zika/``.

Run the default workflow
========================

The zika :term:`ingest workflow` uses the `NCBI Datasets CLI tools <https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/>`_
to download public data and uses a combination of :doc:`augur curate <augur:usage/cli/curate/index>` and other data manipulation tools to curate
the downloaded data into a format suitable for :term:`phylogenetic workflows <phylogenetic workflow>`.

1. Change directory to the Zika pathogen repository downloaded in the previous step

.. code-block::

    $ cd zika

2. Run the default ingest workflow with the :term:`Nextstrain CLI`.

.. code-block::

    $ nextstrain build ingest
    Using profile profiles/default and workflow specific profile profiles/default for setting default command line arguments.
    Building DAG of jobs…
    [...a lot of output...]

This should take just a few minutes to complete.
There should be two final output files:

* ``ingest/results/metadata.tsv``
* ``ingest/results/sequences.fasta``

The output files should have the same data formats as the public data files hosted by Nextstrain, available at:

* https://data.nextstrain.org/files/workflows/zika/metadata.tsv.zst
* https://data.nextstrain.org/files/workflows/zika/sequences.fasta.zst

Your results may have additional records depending on whether new data has been released since the public data files were last uploaded.


Configuring the ingest workflow
===============================

Now that you've seen the default outputs of the ingest workflow, you can try configuring the ingest workflow to change the outputs.
If you want to see the uncurated NCBI Datasets data to decide what changes you would like to make to the workflow, you can run the following:

.. include:: ../../snippets/uncurated-ncbi-dataset.rst

We'll walk through an example custom config to include an additional column in the curated output.
For example, examining the raw NCBI metadata shows us that ``virus-name`` is a NCBI Datasets field that is not currently downloaded by the default Zika ingest workflow.
If you wanted this field to be included in your outputs, you could perform the following steps.

1. Create a new build config directory ``ingest/build-configs/tutorial/``

.. code-block::

    $ mkdir ingest/build-configs/tutorial

2. Create a new config file ``ingest/build-configs/tutorial/config.yaml``

.. code-block::

    ncbi_datasets_fields:
      - accession
      - sourcedb
      - sra-accs
      - isolate-lineage
      - geo-region
      - geo-location
      - isolate-collection-date
      - release-date
      - update-date
      - length
      - host-name
      - isolate-lineage-source
      - biosample-acc
      - submitter-names
      - submitter-affiliation
      - submitter-country
      - virus-name

    curate:
      field_map:
        virus-name: virus_name
      metadata_columns:
        - genbank_accession
        - genbank_accession_rev
        - strain
        - date
        - region
        - country
        - division
        - location
        - length
        - host
        - release_date
        - update_date
        - sra_accessions
        - authors
        - institution
        - virus_name

.. note::

    Config parameters that are dictionaries will merge with the parameters defined in ``ingest/defaults/config.yaml``
    while all other types will overwrite the default.
    See `Snakemake documentation <https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html>`_ for more details on how configuration files work.

This config adds ``virus-name`` to the ``ncbi_datasets_fields`` to make the workflow parse the column from the downloaded NCBI data.
The ``curate.field_map`` entry renames the field from ``virus-name`` to ``virus_name`` to match the underscore naming scheme of column names.
Finally, adding ``virus_name`` to the ``curate.metadata_columns`` configures the workflow to include the new column in the final output file.

All config parameters available are listed in the ``ingest/defaults/config.yaml`` file.
Any of the config parameters can be overridden in a custom config file.

3. Run the ingest workflow again with the custom config file.

.. code-block::

    $ nextstrain build ingest --configfile build-configs/tutorial/config.yaml --forceall
    Using profile profiles/default and workflow specific profile profiles/default for setting default command line arguments.
    Config file defaults/config.yaml is extended by additional config specified via the command line.
    Building DAG of jobs…
    [...a lot of output...]

4. Inspect the new ``ingest/results/metadata.tsv`` to see that it now includes the additional ``virus_name`` column.

Advanced usage: Customizing the ingest workflow
===============================================

.. note::

    This section of the tutorial requires an understanding of `Snakemake <https://snakemake.readthedocs.io/en/stable/>`_ workflows.

In addition to configuring the ingest workflow, it is also possible to extend the ingest workflow with your own custom steps.
We'll walk through an example customization that joins additional metadata to the public data that you've curated in the previous steps.

1. Create an additional metadata file ``ingest/build-configs/tutorial/additional-metadata.tsv``

.. code-block::

    genbank_accession    column_A    column_B    column_C
    AF013415    AAAAA    BBBBB    CCCCC
    AF372422    AAAAA    BBBBB    CCCCC
    AY326412    AAAAA    BBBBB    CCCCC
    AY632535    AAAAA    BBBBB    CCCCC
    EU303241    AAAAA    BBBBB    CCCCC
    EU074027    AAAAA    BBBBB    CCCCC
    EU545988    AAAAA    BBBBB    CCCCC
    NC_012532    AAAAA    BBBBB    CCCCC
    DQ859059    AAAAA    BBBBB    CCCCC
    JN860885    AAAAA    BBBBB    CCCCC


2. Create a new rules file ``ingest/build-configs/tutorial/merge-metadata.smk``

.. code-block::

    rule merge_metadata:
      input:
        metadata="results/metadata.tsv",
        additional_metadata="build-configs/tutorial/additional-metadata.tsv",
      output:
        merged_metadata="results/merged-metadata.tsv"
      shell:
        """
        tsv-join -H \
          --filter-file {input.additional_metadata} \
          --key-fields "genbank_accession" \
          --append-fields "*" \
          --write-all "?" \
          {input.metadata} > {output.merged_metadata}
        """

This rule uses `tsv-join <https://github.com/eBay/tsv-utils/blob/master/docs/tool_reference/tsv-join.md>`_ to merge the
additional metadata with the metadata output from the ingest workflow.
The records will be merged using the ``genbank_accession`` column and all fields from the ``additional-metadata.tsv``
file will be appended to the metadata.
Any record in the ``metadata.tsv`` that does not have a matching record in the ``additional-metadata.tsv`` will have a
default ``?`` value in the new columns.

3. Add the following to the custom config file ``ingest/build-configs/tutorial/config.yaml``

.. code-block::

    custom_rules:
      - build-configs/tutorial/merge-metadata.smk

The ``custom_rules`` config tells the ingest workflow to include your custom rules so that you can run them as part of the workflow.

4. Run the ingest workflow again with the customized rule.

.. code-block::

    $ nextstrain build ingest merge_metadata --configfile build-configs/tutorial/config.yaml
    Using profile profiles/default and workflow specific profile profiles/default for setting default command line arguments.
    Config file config/defaults.yaml is extended by additional config specified via the command line.
    Building DAG of jobs...
    [...a lot of output...]

5. Inspect the ``ingest/results/merged-metadata.tsv`` file to see that it includes the additional columns ``column_A``, ``column_B``, and ``column_C``.
The records with the ``genbank_accession`` listed in the ``additional-metadata.tsv`` file should have the placeholder data in the new columns,
while other records should have the default ``?`` value.

Next steps
==========

* Run the `zika phylogenetic workflow <https://github.com/nextstrain/zika/tree/main/phylogenetic>`_ with new ingested data as input
  by running

  .. code-block::

      $ mv ingest/results/* phylogenetic/data/
      $ nextstrain build phylogenetic

* :doc:`Learn how to create an ingest workflow </tutorials/creating-a-pathogen-repo/creating-an-ingest-workflow>`
