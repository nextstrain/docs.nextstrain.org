===============================
Using Pathoplexus in Nextstrain
===============================

.. ATTENTION::

   When using Pathoplexus (PPX) as a data source, please review the latest
   `PPX Data Use Terms`_. This guide is intended to give recommendations for how
   to use PPX data in Nextstrain workflows following the Nextstrain team's
   interpretation of the `PPX Data Use Terms`_ as of January 26, 2026.

   **Please take special care to comply with the** `RESTRICTED Data Use terms`_
   - if you used RESTRICTED data you need to create and cite a DOI and may
   have authorship obligations.

This page is for users who are already familiar with the following:

* `Pathoplexus (PPX) <https://pathoplexus.org/>`__
* :doc:`/tutorials/creating-a-pathogen-repo/creating-an-ingest-workflow`
* :doc:`/tutorials/creating-a-phylogenetic-workflow`

This guide will refer to the `RSV repository <https://github.com/nextstrain/rsv>`__
as the example Nextstrain repository for using PPX data.

.. contents:: Table of Contents
   :local:
   :depth: 2

Ingest Workflow
===============

Data Source
-----------

Fetch data from the PPX `LAPIS query engines`_ that are available per pathogen.
Define the URLs in the workflow config, with query parameters to download the
metadata in the CSV format and only include the ``LATEST_VERSION`` of records:

.. code-block:: yaml

   ppx_fetch:
      a:
         seqs: https://lapis.pathoplexus.org/rsv-a/sample/unalignedNucleotideSequences?versionStatus=LATEST_VERSION
         meta: https://lapis.pathoplexus.org/rsv-a/sample/details?dataFormat=csv&versionStatus=LATEST_VERSION
      b:
         seqs: https://lapis.pathoplexus.org/rsv-b/sample/unalignedNucleotideSequences?versionStatus=LATEST_VERSION
         meta: https://lapis.pathoplexus.org/rsv-b/sample/details?dataFormat=csv&versionStatus=LATEST_VERSION
      
Use an additional config param ``ppx_metadata_fields`` to define a subset
of fields to include in the metadata to reduce the size the downloaded file.
General metadata fields such as ``sampleCollectionDate`` are standardized across
pathogens, but please refer to the `LAPIS query engines`_ to see pathogen specific fields. 

Curation
--------

The PPX data curation steps are similar to the :ref:`NCBI curation steps <curation-steps>`
with the main differences below.

Add accession URLs
~~~~~~~~~~~~~~~~~~

It is important to add the URLs for the PPX and INSDC accessions during curation
to be included in the final metadata TSV and the phylogenetic dataset.

+------------------+----------------------+------------------------------------------------------------+
| Accession field  | URL field            | URL                                                        |
+==================+======================+============================================================+
| PPX_accession    | PPX_accession__url   | ``https://pathoplexus.org/seq/<PPX_accession>``            |
+------------------+----------------------+------------------------------------------------------------+
| INSDC_accession  | INSDC_accession__url | ``https://www.ncbi.nlm.nih.gov/nuccore/<INSDC_accession>`` |
+------------------+----------------------+------------------------------------------------------------+

The RSV repo uses a custom `curate-urls script`_ to add the URLs.

Geolocation fields
~~~~~~~~~~~~~~~~~~

PPX follows `INSDC geo_loc_name standards`_ which only standardizes country names.
Nextstrain tries to standardized region, country, division, and locations
so this requires additional curation for geolocation fields.

Instead of using the ``augur curate parse-genbank-location`` command, RSV uses
a custom `parse-ppx-division script`_ to split the PPX ``geoLocAdmin1`` field
into ``division`` and ``location`` fields. These can then be standardized with
the geolocation rules via ``augur curate apply-geolocation-rules``.

Starting with `Augur v31.4.0`_, default geolocation rules shipped with Augur also
adds region per country.

Onward data sharing
-------------------

.. Important::

   Even if you do not plan to share the ingest outputs, the metadata for a
   Nextstrain dataset is available for download within Auspice. This is also
   considered onward data sharing!
   
   The metadata TSV is **required** to include these columns to adhere
   to the `PPX Data Use Terms`_

      * PPX_accession 
      * PPX_accession__url
      * INSDC_accession
      * INSDC_accession__url
      * dataUseTerms
      * dataUseTerms__url
      * restrictedUntil

Nextstrain automated workflows upload the outputs to a public S3 bucket, where
the default files are only OPEN data and the RESTRICTED data are in separate files.
This is reflected in the inputs of the phylogenetic workflow.

Phylogenetic Workflow
=====================

The phylogenetic workflow does not require significant modification to use PPX data.
The only parts that will need to be changed are the inputs and the ``augur export`` step.

Inputs
------

.. ATTENTION::

   If you are using the RESTRICTED data for your own analysis,
   please take special care to comply with the `RESTRICTED Data Use terms`_.

The default inputs for Nextstrain pathogens include both the OPEN and RESTRICTED
data to utilize all available PPX data:

.. code-block:: yaml

   inputs:
      - name: ppx_open
        metadata: "https://data.nextstrain.org/files/workflows/rsv/{a_or_b}/metadata.tsv.gz"
        sequences: "https://data.nextstrain.org/files/workflows/rsv/{a_or_b}/sequences.fasta.xz"
      - name: ppx_restricted
        metadata: "https://data.nextstrain.org/files/workflows/rsv/{a_or_b}/metadata_restricted.tsv.gz"
        sequences: "https://data.nextstrain.org/files/workflows/rsv/{a_or_b}/sequences_restricted.fasta.xz"

Augur export
------------

The ``augur export`` step that produces the Nextstrain dataset needs to adhere
to `PPX Data Use Terms`_ for both web display and onward data sharing since the
metadata is available for download within Auspice.

Auspice config
~~~~~~~~~~~~~~

The Auspice config should include the proper attributions for PPX:

1. Include Pathoplexus as a ``data_provenance``
2. Add ``dataUseTerms`` as a coloring option
3. Include additional metadata columns ``PPX_accession``, ``INSDC_accession``, ``restrictedUntil``.
   Starting with `Augur v31.4.0`_, the associated ``*__url`` columns should be
   automatically exported with the metadata columns.

.. code-block:: json

   {
      "data_provenance": [
         {
            "name": "Pathoplexus",
            "url": "https://pathoplexus.org"
         }
      ],
      "colorings": [
         {
            "key": "dataUseTerms",
            "title": "Data use terms",
            "type": "categorical"
         }
      ],
      "metadata_columns": [
         "PPX_accession",
         "INSDC_accession",
         "restrictedUntil"
      ]
   }

Description
~~~~~~~~~~~

It is strongly encouraged to include a ``description.md`` that acknowledges
PPX as the data source and point to any provisioned data files.
Please see the example in the `RSV description`_.

Updating existing workflows
===========================

If you are updating an existing workflow that previously used NCBI as a data source,
do the following updates in addition to the changes above.

1. Update all NCBI accessions to PPX accessions in configuration files, e.g.
   ingest annotations.tsv and phylogenetic include/exclude files.
   This can be done programmatically with the new ingest output as documented
   in `WNV <https://github.com/nextstrain/WNV/commit/34ea83efef9dbd4d3278a5339af8a1990fc60f80>`__.
2. If using example data for CI tests, update the data to PPX OPEN records.
3. To reduce confusion of the data source, remove NCBI related config params,
   scripts, and Snakemake rules.

.. _Augur v31.4.0: https://github.com/nextstrain/augur/releases/tag/31.4.0
.. _curate-urls script: https://github.com/nextstrain/rsv/blob/fc6c095c3983d9f53eafdb3b68cace7d76d517e4/ingest/bin/curate-urls.py
.. _INSDC geo_loc_name standards: https://www.insdc.org/submitting-standards/geo_loc_name-qualifier-vocabulary
.. _LAPIS query engines: https://pathoplexus.org/api-documentation
.. _parse-ppx-division script: https://github.com/nextstrain/rsv/blob/fc6c095c3983d9f53eafdb3b68cace7d76d517e4/ingest/bin/parse-ppx-division
.. _PPX Data Use Terms: https://pathoplexus.org/about/terms-of-use/data-use-terms
.. _RESTRICTED Data Use terms: https://pathoplexus.org/about/terms-of-use/data-use-terms#42-restricted-data-use
.. _RSV description: https://github.com/nextstrain/rsv/blob/fc6c095c3983d9f53eafdb3b68cace7d76d517e4/config/description.md#L24-L36
