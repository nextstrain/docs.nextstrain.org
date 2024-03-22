.. code-block::

    $ nextstrain shell .
    $ datasets download virus genome taxon <taxon-id> --filename ingest/data/ncbi_dataset.zip
    $ dataformat tsv virus-genome --package ingest/data/ncbi_dataset.zip > ingest/data/raw_metadata.tsv
    $ exit

The produced ``ingest/data/raw_metadata.tsv`` will contain all of the fields available from NCBI Datasets.
Note that the headers in this file use the human readable ``Name`` of the
`NCBI Datasets' available fields <https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/dataformat/tsv/dataformat_tsv_virus-genome/#fields>`_,
while the pipeline uses the config's ``curate.field_map`` dictionary to convert these to computer friendly ``Mnemonic``.
