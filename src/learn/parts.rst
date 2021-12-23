================
Parts of a whole
================

Nextstrain is made up of many different parts that all work together.  Two core
parts are :term:`Augur` and :term:`Auspice`.

.. graphviz::
    :align: center

    digraph {
        graph [
            rankdir=LR,
        ];

        node [
            shape=box,
            style="rounded, filled",
            fontname="Lato, 'Helvetica Neue', sans-serif",
            fontsize=12,
            height=0.1,
            colorscheme=paired10,
        ];

        edge [
            arrowhead=open,
            arrowsize=0.75,
        ];

        Augur [fillcolor=1, color=2];
        Auspice [fillcolor=3, color=4];

        Augur -> Auspice;
    }

:term:`Augur` is a series of composable, modular bioinformatics tools. We use these
to create recipes for different pathogens and different analyses, which can be
reproduced given the same input data and replicated when new data is available.

.. graphviz::
    :align: center

    graph {
        graph [
            ranksep=0.25,
        ];

        node [
            shape=box,
            style="rounded, filled",
            fontname="Lato, 'Helvetica Neue', sans-serif",
            fontsize=12,
            height=0.1,
            colorscheme=paired10,
            fillcolor=1,
            color=2,
        ];

        edge [
            arrowhead=open,
            arrowsize=0.75,
        ];

        Augur -- ellipsis1 [style=invis];
        ellipsis1 [label="…", shape=plain, style=""];

        Augur -- {filter, align, tree, refine, export};

        Augur -- ellipsis2 [style=invis];
        ellipsis2 [label="…", shape=plain, style=""];
    }

:term:`Auspice` is a web-based visualization program, to present and interact with
phylogenomic and phylogeographic data. Auspice is what you see when, for
example, you visit `nextstrain.org/mumps/na
<https://nextstrain.org/mumps/na>`__.

.. figure:: /images/mumps.png

    Auspice displaying Mumps genomes from North America.

Augur produces :term:`datasets<dataset>` which are
visualized by Auspice.  These files are often referred to as :term:`JSONs`
colloquially because they use a generic data format called JSON.

.. graphviz::
    :align: center

    digraph {
        graph [
            rankdir=LR,
        ];

        node [
            shape=box,
            style="rounded, filled",
            fontname="Lato, 'Helvetica Neue', sans-serif",
            fontsize=12,
            height=0.1,
            colorscheme=paired10,
        ];

        edge [
            arrowhead=open,
            arrowsize=0.75,
        ];

        Augur [fillcolor=1, color=2];
        Auspice [fillcolor=3, color=4];
        jsons [label="mumps_na.json\lmumps_na_root-sequence.json"];

        Augur -> jsons -> Auspice;
    }

:term:`Builds<build>` are recipes of code and data that produce these :term:`datasets<dataset>`.

.. graphviz::
    :align: center

    digraph {
        graph [
            ranksep=0.25,
        ];

        node [
            shape=box,
            style="rounded, filled",
            fontname="Lato, 'Helvetica Neue', sans-serif",
            fontsize=12,
            height=0.1,
            colorscheme=paired10,
        ];

        edge [
            arrowhead=open,
            arrowsize=0.75,
        ];

        subgraph Augur {
            graph [rank=same];
            node [fillcolor=1, color=2];
            filter -> align -> tree -> refine -> export;
        }

        Auspice [fillcolor=3, color=4];

        export -> Auspice;

        subgraph inputs {
            graph [rank=same];
            sequences [label="sequences.fasta"];
            metadata [label="metadata.tsv"];
        }

        sequences -> filter;
        metadata -> filter;
    }

Builds run several commands and are often automated by workflow managers such as `Snakemake <https://snakemake.readthedocs.io>`__, `Nextflow <https://nextflow.io>`__ and `WDL <https://openwdl.org>`__. A :term:`workflow` bundles one or more related :term:`builds<build>` which each produce a :term:`dataset` for visualization with :term:`Auspice`.

As an example, our core workflows are organized as `Git repositories <https://git-scm.com>`__ hosted on `GitHub <https://github.com/nextstrain>`__. Each contains a :doc:`Snakemake workflow </guides/bioinformatics/augur_snakemake>` using Augur, configuration, and data.

.. graphviz::
    :align: center

    digraph {
        node [shape=box]
        rankdir=LR

        subgraph cluster_0 {
            label = "Zika workflow";
            build0 [label="zika"]
        }

        subgraph cluster_1 {
            label = "SARS-CoV-2 workflow";
            build1 [label="ncov/global"]
            build2 [label="ncov/africa"]
        }

        // invisible edge to arrange clusters on same row
        {
            edge[style=invis]
            build0 -> build1
        }
    }

`nextstrain.org <https://nextstrain.org>`__ is a web application to host and
present the core pathogen builds maintained by the Nextstrain team, as well as
builds published to :doc:`Nextstrain Groups </guides/share/nextstrain-groups>`
and :doc:`community pages </guides/share/community-builds>` which are
maintained and :doc:`shared </guides/share/index>` by many other people.  The
website incorporates a customized version of Auspice for displaying each
dataset.

You can run :term:`Augur` and :term:`Auspice` on
your own computer and use them independently or together with your own builds,
our core builds, or others' group or community builds.  You can even install
Auspice on :doc:`your own web server <auspice:server/index>` if you don't want
to host your builds via nextstrain.org.

The :term:`Nextstrain CLI<CLI>` ties
together all of the above to provide a consistent way to run pathogen builds,
access Nextstrain tools like Augur and Auspice across computing environments
such as Docker, Conda, and AWS Batch, and publish datasets to nextstrain.org.

:doc:`Nextclade <nextclade:index>` is a web application and two command-line
programs (``nextclade`` and ``nextalign``) for performing viral genome
alignment, mutation calling, clade assignment, quality checks, and phylogenetic
placement.  Nextclade can be used indepedently of other Nextstrain tools as
well as integrated into builds.

With this overview, you'll be better prepared to :doc:`install Nextstrain
</install>` and :doc:`run a build </tutorials/quickstart>` or :doc:`contribute
to development </guides/contribute/index>`.
