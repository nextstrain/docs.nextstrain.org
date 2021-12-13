==============================
Exploring Zika virus evolution
==============================

This tutorial explains how to create `a Nextstrain build <https://docs.nextstrain.org/projects/augur/en/stable/faq/what-is-a-build.html>`__ for the Zika virus. We will first make the build step-by-step using an example data set. Then we will see how to automate this stepwise process by defining a pathogen build script.

.. contents:: Table of Contents
   :local:

Setup
=====

`Install Nextstrain <../install>`__ and `check out the quickstart <./quickstart>`__. These instructions will install all of the software you need to complete this tutorial.

Once you've installed Nextstrain, activate the Nextstrain environment.

::

   conda activate nextstrain

Build steps
===========

Nextstrain builds typically require the following steps:

1. Prepare pathogen sequences and metadata
2. Align sequences
3. Construct a phylogeny from aligned sequences
4. Annotate the phylogeny with inferred ancestral pathogen dates, sequences, and traits
5. Export the annotated phylogeny and corresponding metadata into auspice-readable format

Download the Zika pathogen build which includes example data and a pathogen build script.

::

   git clone https://github.com/nextstrain/zika-tutorial.git
   cd zika-tutorial

Optionally, if you want to run this tutorial from the Nextstrain Docker image, start Docker and then enter a shell prompt on that image.

::

   nextstrain shell .

Note the dot (``.``) as the last argument; it is important and indicates that your current directory (``zika-tutorial/``) is the build directory. Your command prompt will change to indicate you are in the build environment. If you want to leave the build environment, run the command ``exit``.

Prepare the Sequences
=====================

A Nextstrain build typically starts with a collection of pathogen sequences in a single `FASTA <https://en.wikipedia.org/wiki/FASTA_format>`__ file and a corresponding table of metadata describing those sequences in a tab-delimited text file. For this tutorial, we will use an example data set with a subset of 34 viruses.

Each example virus sequence record looks like the following, with the virus's strain ID as the sequence name in the header line followed by the virus sequence.

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
-------------------

Precalculate the composition of the sequences (e.g., numbers of nucleotides, gaps, invalid characters, and total sequence length) prior to filtering. The resulting sequence index speeds up subsequent filter steps especially in more complex workflows.

::

   mkdir -p results/

   augur index \
     --sequences data/sequences.fasta \
     --output results/sequence_index.tsv

The first lines in the sequence index look like this.

::

   strain  length  A   C   G   T   N   other_IUPAC -   ?   invalid_nucleotides
   PAN/CDC_259359_V1_V3/2015   10771   2952    2379    3142    2298    0   0   0   0   0
   COL/FLR_00024/2015  10659   2921    2344    3113    2281    0   0   0   0   0
   PRVABC59    10675   2923    2351    3115    2286    0   0   0   0   0
   COL/FLR_00008/2015  10659   2924    2344    3110    2281    0   0   0   0   0

Filter the Sequences
--------------------

Filter the parsed sequences and metadata to exclude strains from subsequent analysis and subsample the remaining strains to a fixed number of samples per group.

::

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
-------------------

Create a multi-sequence alignment using a custom reference. After this alignment, columns with gaps in the reference are removed. Additionally, the ``--fill-gaps`` flag fills gaps in non-reference sequences with “N” characters. These modifications force all sequences into the same coordinate space as the reference sequence.

::

   augur align \
     --sequences results/filtered.fasta \
     --reference-sequence config/zika_outgroup.gb \
     --output results/aligned.fasta \
     --fill-gaps

Now the pathogen sequences are ready for analysis.

Construct the Phylogeny
=======================

Infer a phylogenetic tree from the multi-sequence alignment.

::

   augur tree \
     --alignment results/aligned.fasta \
     --output results/tree_raw.nwk

The resulting tree is stored in `Newick format <http://evolution.genetics.washington.edu/phylip/newicktree.html>`__. Branch lengths in this tree measure nucleotide divergence.

Get a Time-Resolved Tree
------------------------

Augur can also adjust branch lengths in this tree to position tips by their sample date and infer the most likely time of their ancestors, using `TreeTime <https://github.com/neherlab/treetime>`__. Run the ``refine`` command to apply TreeTime to the original phylogenetic tree and produce a “time tree”.

::

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
======================

Reconstruct Ancestral Traits
----------------------------

TreeTime can also infer ancestral traits from an existing phylogenetic tree and the metadata annotating each tip of the tree. The following command infers the region and country of all internal nodes from the time tree and original strain metadata. As with the ``refine`` command, the resulting JSON output is indexed by strain or internal node name.

::

   augur traits \
     --tree results/tree.nwk \
     --metadata data/metadata.tsv \
     --output-node-data results/traits.json \
     --columns region country \
     --confidence

Infer Ancestral Sequences
-------------------------

Next, infer the ancestral sequence of each internal node and identify any nucleotide mutations on the branches leading to any node in the tree.

::

   augur ancestral \
     --tree results/tree.nwk \
     --alignment results/aligned.fasta \
     --output-node-data results/nt_muts.json \
     --inference joint

Identify Amino-Acid Mutations
-----------------------------

Identify amino acid mutations from the nucleotide mutations and a reference sequence with gene coordinate annotations. The resulting JSON file contains amino acid mutations indexed by strain or internal node name and by gene name. To export a FASTA file with the complete amino acid translations for each gene from each node's sequence, specify the ``--alignment-output`` parameter in the form of ``results/aligned_aa_%GENE.fasta``.

::

   augur translate \
     --tree results/tree.nwk \
     --ancestral-sequences results/nt_muts.json \
     --reference-sequence config/zika_outgroup.gb \
     --output-node-data results/aa_muts.json

Export the Results
==================

Finally, collect all node annotations and metadata and export it in Auspice's JSON format. This refers to three config files to define colors via ``config/colors.tsv``, latitude and longitude coordinates via ``config/lat_longs.tsv``, as well as page title, maintainer, filters present, etc., via ``config/auspice_config.json``. The resulting tree and metadata JSON files are the inputs to the Auspice visualization tool.

::

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

Visualize the Results
=====================

If you entered the Nextstrain build environment using ``nextstrain shell`` at the beginning of this tutorial, leave it now using the ``exit`` command and then use ``nextstrain view`` to visualize the Zika build output in ``auspice/*.json``.

::

   # Leave the shell you entered earlier.
   exit

   # View results in your auspice/ directory.
   nextstrain view auspice/

If you're not using the Nextstrain CLI shell, start auspice to view the dataset in the Zika build output directory.

::

   auspice view --datasetDir auspice

When Auspice is running, navigate to http://localhost:4000/local/zika in your browser to view the results.

To stop Auspice and return to the command line when you are done viewing your data, press CTRL+C.

Automate the Build with Snakemake
=================================

While it is instructive to run all of the above commands manually, it is more practical to automate their execution with a single script. Nextstrain implements these automated pathogen builds with `Snakemake <https://snakemake.readthedocs.io>`__ by defining a ``Snakefile`` like `the one in the Zika repository you downloaded <https://github.com/nextstrain/zika-tutorial/blob/master/Snakefile>`__.

From the ``zika-tutorial/`` directory, delete the output from the manual steps above.

::

   rm -rf results/ auspice/

Run the automated build.

::

   nextstrain build --cpus 1 .

This runs all of the manual steps above up through the auspice export. View the results the same way you did before to confirm it produced the same Zika build you made manually.

Note that automated builds will only re-run steps when the data changes. This means builds will pick up where they left off if they are restarted after being interrupted. If you want to force a re-run of the whole build, first remove any previous output with ``nextstrain build --cpus 1 . clean``.

Next steps
==========

-  Learn more about `Augur commands <https://docs.nextstrain.org/projects/augur/en/stable/index.html>`__.
-  Learn more about `Auspice visualizations <https://docs.nextstrain.org/projects/auspice/en/stable/>`__.
-  Fork the `Zika tutorial pathogen repository on GitHub <https://github.com/nextstrain/zika-tutorial>`__, modify the Snakefile to make your own pathogen build, and learn `how to contribute to nextstrain.org <../guides/share/community-builds>`__.
