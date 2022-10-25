============================
Creating a pathogen workflow
============================

This tutorial dissects the :term:`single-build workflow<workflow>` used in the previous tutorial. We will first make the build step-by-step. Then we will automate this stepwise process in a :term:`workflow`.

.. note::

   The difference between a :term:`workflow` and :term:`build` isn't obvious with single-build workflows such as this example Zika workflow, but will become more distinct in multi-build workflows such as the SARS-CoV-2 workflow.

.. contents:: Table of Contents
   :local:
   :depth: 2

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`.
2. Run through the :doc:`previous tutorial<running-a-workflow>`. This will verify your installation.

Setup
=====

1. Change directory to the Zika :term:`workflow repository` downloaded in the previous tutorial.

   .. code-block:: bash

      cd zika-tutorial

2. Create a folder for results.

   .. code-block:: bash

      mkdir -p results/

3. Additionally, if you installed Nextstrain with the :term:`Docker runtime<runtime>`, start Docker and enter the runtime.

   .. code-block:: bash

      nextstrain shell .

   .. note::

      The dot (``.``) as the last argument indicates that your current directory (``zika-tutorial/``) is the working directory. Your command prompt will change to indicate you are in the Docker runtime. If you want to leave the runtime, run the command ``exit``.

Run a Nextstrain Build
======================

:term:`Nextstrain builds<build>` typically require the following steps:

.. contents::
   :local:

Prepare the Sequences
---------------------


A :term:`Nextstrain build<build>` typically starts with a collection of pathogen sequences in a single `FASTA <https://en.wikipedia.org/wiki/FASTA_format>`_ file and a corresponding table of metadata describing those sequences in a tab-delimited text file. For this tutorial, we will use example data containing 34 virus sequences.

Each virus sequence record looks like the following, with the virus's strain ID as the sequence name in the header line followed by the virus sequence.

::

   >PAN/CDC_259359_V1_V3/2015
   gaatttgaagcgaatgctaacaacagtatcaacaggttttattttggatttggaaacgag
   agtttctggtcatgaaaaacccaaaaaagaaatccggaggattccggattgtcaatatgc
   taaaacgcggagtagcccgtgtgagcccctttgggggcttgaagaggctgccagccggac
   ttctgctgggtcatgggcccatcaggatggtcttggcgattctagcctttttgagattca

Each sequence record's virus strain ID links to the tab-delimited metadata file by the latter's ``strain`` field. The metadata file contains a header of column names followed by one row per virus strain ID in the sequences file. An example metadata file looks like the following.

::

   strain  virus   accession   date    region  country division    city    db  segment authors url title   journal paper_url
   1_0087_PF   zika    KX447509    2013-12-XX  oceania french_polynesia    french_polynesia    french_polynesia    genbank genome  Pettersson et al    https://www.ncbi.nlm.nih.gov/nuccore/KX447509   How Did Zika Virus Emerge in the Pacific Islands and Latin America? MBio 7 (5), e01239-16 (2016)    https://www.ncbi.nlm.nih.gov/pubmed/27729507
   1_0181_PF   zika    KX447512    2013-12-XX  oceania french_polynesia    french_polynesia    french_polynesia    genbank genome  Pettersson et al    https://www.ncbi.nlm.nih.gov/nuccore/KX447512   How Did Zika Virus Emerge in the Pacific Islands and Latin America? MBio 7 (5), e01239-16 (2016)    https://www.ncbi.nlm.nih.gov/pubmed/27729507
   1_0199_PF   zika    KX447519    2013-11-XX  oceania french_polynesia    french_polynesia    french_polynesia    genbank genome  Pettersson et al    https://www.ncbi.nlm.nih.gov/nuccore/KX447519   How Did Zika Virus Emerge in the Pacific Islands and Latin America? MBio 7 (5), e01239-16 (2016)    https://www.ncbi.nlm.nih.gov/pubmed/27729507
   Aedes_aegypti/USA/2016/FL05 zika    KY075937    2016-09-09  north_america   usa usa usa genbank genome  Grubaugh et al  https://www.ncbi.nlm.nih.gov/nuccore/KY075937   Genomic epidemiology reveals multiple introductions of Zika virus into the United States    Nature (2017) In press  https://www.ncbi.nlm.nih.gov/pubmed/28538723

A metadata file must have the following columns:

-  Strain
-  Virus
-  Date

Builds using published data should include the following additional columns, as shown in the example above:

-  Accession (e.g., NCBI GenBank, EMBL EBI, etc.)
-  Authors
-  URL
-  Title
-  Journal
-  Paper_URL

Index the Sequences
~~~~~~~~~~~~~~~~~~~

Precalculate the composition of the sequences (e.g., numbers of nucleotides, gaps, invalid characters, and total sequence length) prior to filtering. The resulting sequence index speeds up subsequent filter steps especially in more complex workflows.

.. code-block:: bash

   augur index \
     --sequences data/sequences.fasta \
     --output results/sequence_index.tsv

The first lines in ``results/sequence_index.tsv`` should look like this.

::

   strain  length  A   C   G   T   N   other_IUPAC -   ?   invalid_nucleotides
   PAN/CDC_259359_V1_V3/2015   10771   2952    2379    3142    2298    0   0   0   0   0
   COL/FLR_00024/2015  10659   2921    2344    3113    2281    0   0   0   0   0
   PRVABC59    10675   2923    2351    3115    2286    0   0   0   0   0
   COL/FLR_00008/2015  10659   2924    2344    3110    2281    0   0   0   0   0

Filter the Sequences
~~~~~~~~~~~~~~~~~~~~

Filter the parsed sequences and metadata to exclude strains from subsequent analysis and subsample the remaining strains to a fixed number of samples per group.

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --sequence-index results/sequence_index.tsv \
     --metadata data/metadata.tsv \
     --exclude config/dropped_strains.txt \
     --output results/filtered.fasta \
     --group-by country year month \
     --sequences-per-group 20 \
     --min-date 2012

Align the Sequences
~~~~~~~~~~~~~~~~~~~

Create a multi-sequence alignment using a custom reference. After this alignment, columns with gaps in the reference are removed. Additionally, the ``--fill-gaps`` flag fills gaps in non-reference sequences with “N” characters. These modifications force all sequences into the same coordinate space as the reference sequence.

.. code-block:: bash

   augur align \
     --sequences results/filtered.fasta \
     --reference-sequence config/zika_outgroup.gb \
     --output results/aligned.fasta \
     --fill-gaps

Now the pathogen sequences are ready for analysis.

Construct the Phylogeny
-----------------------

Infer a phylogenetic tree from the multi-sequence alignment.

.. code-block:: bash

   augur tree \
     --alignment results/aligned.fasta \
     --output results/tree_raw.nwk

The resulting tree is stored in `Newick format <http://evolution.genetics.washington.edu/phylip/newicktree.html>`_. Branch lengths in this tree measure nucleotide divergence.

Get a Time-Resolved Tree
~~~~~~~~~~~~~~~~~~~~~~~~

Augur can also adjust branch lengths in this tree to position tips by their sample date and infer the most likely time of their ancestors, using `TreeTime <https://github.com/neherlab/treetime>`_. Run the ``refine`` command to apply TreeTime to the original phylogenetic tree and produce a “time tree”.

.. code-block:: bash

   augur refine \
     --tree results/tree_raw.nwk \
     --alignment results/aligned.fasta \
     --metadata data/metadata.tsv \
     --output-tree results/tree.nwk \
     --output-node-data results/branch_lengths.json \
     --timetree \
     --coalescent opt \
     --date-confidence \
     --date-inference marginal \
     --clock-filter-iqd 4

In addition to assigning times to internal nodes, the ``refine`` command filters tips that are likely outliers and assigns confidence intervals to inferred dates. Branch lengths in the resulting Newick tree measure adjusted nucleotide divergence. All other data inferred by TreeTime is stored by strain or internal node name in the corresponding JSON file.

Annotate the Phylogeny
----------------------

Reconstruct Ancestral Traits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TreeTime can also infer ancestral traits from an existing phylogenetic tree and the metadata annotating each tip of the tree. The following command infers the region and country of all internal nodes from the time tree and original strain metadata. As with the ``refine`` command, the resulting JSON output is indexed by strain or internal node name.

.. code-block:: bash

   augur traits \
     --tree results/tree.nwk \
     --metadata data/metadata.tsv \
     --output-node-data results/traits.json \
     --columns region country \
     --confidence

Infer Ancestral Sequences
~~~~~~~~~~~~~~~~~~~~~~~~~

Next, infer the ancestral sequence of each internal node and identify any nucleotide mutations on the branches leading to any node in the tree.

.. code-block:: bash

   augur ancestral \
     --tree results/tree.nwk \
     --alignment results/aligned.fasta \
     --output-node-data results/nt_muts.json \
     --inference joint

Identify Amino-Acid Mutations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify amino acid mutations from the nucleotide mutations and a reference sequence with gene coordinate annotations. The resulting JSON file contains amino acid mutations indexed by strain or internal node name and by gene name. To export a FASTA file with the complete amino acid translations for each gene from each node's sequence, specify the ``--alignment-output`` parameter in the form of ``results/aligned_aa_%GENE.fasta``.

.. code-block:: bash

   augur translate \
     --tree results/tree.nwk \
     --ancestral-sequences results/nt_muts.json \
     --reference-sequence config/zika_outgroup.gb \
     --output-node-data results/aa_muts.json

Export the Results
------------------

Finally, collect all node annotations and metadata and export it in Auspice's JSON format. This refers to three config files to define colors via ``config/colors.tsv``, latitude and longitude coordinates via ``config/lat_longs.tsv``, as well as page title, maintainer, filters present, etc., via ``config/auspice_config.json``. The resulting tree and metadata JSON files are the inputs to the Auspice visualization tool.

.. code-block:: bash

   augur export v2 \
     --tree results/tree.nwk \
     --metadata data/metadata.tsv \
     --node-data results/branch_lengths.json \
                 results/traits.json \
                 results/nt_muts.json \
                 results/aa_muts.json \
     --colors config/colors.tsv \
     --lat-longs config/lat_longs.tsv \
     --auspice-config config/auspice_config.json \
     --output auspice/zika.json

.. note::

   If you entered the Nextstrain Docker runtime using ``nextstrain shell`` at the beginning of this tutorial, leave it now using the ``exit`` command.

   .. code-block:: bash

      # Leave the Docker runtime you entered earlier.
      exit

Visualize the Results
=====================

Use ``nextstrain view`` to visualize the Zika dataset using :term:`Auspice`.

.. code-block:: bash

   nextstrain view auspice/

While Auspice is running, navigate to http://127.0.0.1:4000/zika in your browser to view the dataset.

To stop Auspice and return to the command line when you are done viewing your data, press CTRL+C.

Automate the Build with Snakemake
=================================

While it is instructive to run all of the above commands manually, it is more practical to automate their execution with a workflow manager. Nextstrain implements these automated builds with `Snakemake <https://snakemake.readthedocs.io>`_ by defining a ``Snakefile`` like `this Snakefile <https://github.com/nextstrain/zika-tutorial/blob/master/Snakefile>`_ used in the :doc:`previous tutorial <running-a-workflow>`.

From the ``zika-tutorial/`` directory, delete the previously generated results.

.. code-block:: bash

   rm -rf results/ auspice/

Run the automated build.

.. code-block:: bash

   nextstrain build --cpus 1 .

This runs all of the manual steps above, up through ``augur export``. View the results the same way you did before to confirm it produced the same dataset.

Note that Snakemake will only re-run rules when the data changes. This means workflows will pick up where they left off if they are restarted after being interrupted. If you want to force a re-run of the whole workflow, first remove any previous output with ``nextstrain build --cpus 1 . clean``.

Next steps
==========

-  Learn more about :doc:`Augur commands <augur:index>`.
-  Learn more about :doc:`Auspice visualizations <auspice:index>`.
-  Fork the `Zika tutorial pathogen repository on GitHub <https://github.com/nextstrain/zika-tutorial>`_, modify the Snakefile to make your own pathogen workflow, and learn :doc:`how to contribute to nextstrain.org </guides/share/community-builds>`.
