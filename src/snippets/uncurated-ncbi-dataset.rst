1. Enter an interactive Nextstrain shell to be able to run the NCBI Datasets CLI commands without installing them separately.

.. code-block::

    $ nextstrain shell .

2. Create the ``ingest/data`` directory if it doesn't already exist.

.. code-block::

    $ mkdir -p ingest/data

3. Download the dataset with the pathogen NCBI taxonomy ID.

.. code-block::

    $ datasets download virus genome taxon <taxon-id> \
        --filename ingest/data/ncbi_dataset.zip

4. Extract and format the metadata as a TSV file for easy inspection

.. code-block::

    $ dataformat tsv virus-genome \
        --package ingest/data/ncbi_dataset.zip \
        > ingest/data/raw_metadata.tsv

5. Exit the Nextstrain shell to return to your usual shell environment.

.. code-block::

    $ exit

The produced ``ingest/data/raw_metadata.tsv`` will contain all of the fields available from NCBI Datasets.
Note that the headers in this file use the human readable ``Name`` of the
`NCBI Datasets' available fields <https://www.ncbi.nlm.nih.gov/datasets/docs/v2/reference-docs/command-line/dataformat/tsv/dataformat_tsv_virus-genome/#fields>`_,
while the pipeline uses the config's ``curate.field_map`` dictionary to convert these to computer friendly ``Mnemonic``.
