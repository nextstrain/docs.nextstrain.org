==========
Data files
==========

..  This document started in <https://docs.google.com/document/d/118zKcgUNESszsIfXw08qbubxpA6lJF1RhaMBktY11x0> as the capturing of our decisions around and plans for publishing data files.
    Discussions and other context are linked there.
      -trs, 30 Jan 2023

We publish continually-updated data files associated with our pathogen analyses.
The files show exactly what data is going into and out of our analyses published on `nextstrain.org <https://nextstrain.org>`__.
For others repeating our analyses or doing their own, whether with Nextstrain or not, these data files are useful as ready-made starting points.

This document describes the conventions of the data files we publish: their names, organization, contents, etc.

..  XXX TODO: Discuss expectations/social contract around these files as an
    interface. -trs, 30 Jan 2023

.. note::
    The publishing of our :doc:`SARS-CoV-2 (ncov) workflow's data files <ncov:reference/remote_inputs>` led us to the goal of doing the same for our other pathogen workflows too.
    This work is still in-progress and not all of the examples given below exist yet.
    Furthermore, some of the specific files available for SARS-CoV-2 do not conform to the organization below because they predate it.

At a broad level, we think about two kinds of data files:

Workflow files
    Files which correspond to several :term:`builds <build>` visible on nextstrain.org, e.g. all of builds under <nextstrain.org/ncov/open/…>.
    These often include the full metadata table, sequences FASTA, titer matrix, etc.

    We often call these "inputs" colloquially because they're often the top-level inputs to a :term:`phylogenetic workflow`, but some of the files are actually workflow-level outputs.
    (Albeit, outputs that can be used as time-saving inputs in later workflow runs.)

Build files
    Files which correspond to a specific single :term:`build` visible on nextstrain.org, e.g. <`nextstrain.org/ncov/open/global/6m <https://nextstrain.org/ncov/open/global/6m>`__>.
    These often include the subsampled metadata table, sequences FASTA, and Newick tree as well as the final :term:`dataset` JSONs.

    We often call these "outputs" colloquially because they're produced by running a :term:`phylogenetic workflow`, but some of the files are actually the specific, subsampled inputs that went into the specific build.

Workflow and build files for public data are available from:

  - https\://data.nextstrain.org
  - s3://nextstrain-data
  - gs://nextstrain-data

using the following path structures (with `URL Template <https://datatracker.ietf.org/doc/html/rfc6570>`__-style placeholders emphasized):

.. parsed-literal::

    /files
      /workflows
        **{/workflow-repo}**                (matching github.com/nextstrain{/workflow-repo})
          **{/arbitrary-structure*}**
            /metadata.tsv.zst
            /sequences.fasta.zst
      /datasets
        **{/dataset*}**                     (matching nextstrain.org{/dataset*})
          /metadata.tsv.gz
          /sequences.fasta.zst
          /tree.nwk.gz                (hypothetical)
          /clade-frequencies.tsv.gz   (hypothetical)
          /**{_dataset*}**.json           (e.g. flu_seasonal_h3n2_ha_2y.json)
          /…

Within each :file:`/files/workflows{\{/workflow-repo\}}/…` prefix, each workflow is responsible for the organization and structure of its own files.
Naming conventions and common patterns are used when possible, but different workflows will have different requirements.
For example, the `ncov <https://github.com/nextstrain/ncov>`__ and `seasonal-flu <https://github.com/nextstrain/seasonal-flu>`__ workflows may organize their sequence inputs differently because of the different nature of analyzing SARS-CoV-2 vs. influenza:

.. parsed-literal::

    /files/workflows/ncov/**open/sequences**.fasta.zst

    /files/workflows/seasonal-flu/**h3n2_ha_sequences**.fasta.zst
    /files/workflows/seasonal-flu/**h3n2_na_sequences**.fasta.zst

Within each :file:`/files/datasets{\{/dataset*\}}/…` prefix, we intend to provide a common base set of files, e.g. :file:`metadata.tsv.gz` and :file:`sequences.fasta.zst`, across pathogens and workflows:

.. parsed-literal::

    /files
      /datasets
        /ncov/open/global/6m
          **/metadata.tsv.gz**
          /mutation-summary.tsv.gz

        /flu/seasonal/h3n2/ha/2y
          **/metadata.tsv.gz**
          /titers.tsv

        /dengue/denv2
          **/metadata.tsv.gz**

Extra files beyond the common set are ok and expected.

Although we strive to use fully `open data <https://opendatahandbook.org/guide/en/what-is-open-data/>`__ whenever possible, we cannot always redistribute the data we use.
Files containing private or otherwise restricted data are stored in access-restricted locations with the same structure as above, e.g.:

.. parsed-literal::

    s3://nextstrain-data/files/workflows/ncov/**open**/metadata.tsv.gz
    s3://nextstrain-data/files/datasets/ncov/**open**/global/6m/metadata.tsv.gz

    s3://nextstrain-data-**private**/files/workflows/ncov/**gisaid**/metadata.tsv.gz
    s3://nextstrain-data-**private**/files/datasets/ncov/**gisaid**/global/6m/metadata.tsv.gz
