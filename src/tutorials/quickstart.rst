===========================
Quickstart - Zika evolution
===========================

This tutorial uses the :term:`Nextstrain CLI<CLI>` to help you get started running and viewing :term:`the pathogen builds<Build>` you see on `nextstrain.org <https://nextstrain.org>`_.
It assumes you are comfortable using the command line and installing software on your computer.
If you need help when following this tutorial, please create a post at `discussion.nextstrain.org <https://discussion.nextstrain.org>`_.

In this, you will run a build of `our example Zika analysis <https://github.com/nextstrain/zika-tutorial>`_ and view the results on your computer.
You will have a basic understanding of how to run builds for other pathogens and a foundation for understanding the Nextstrain ecosystem in more depth.

.. contents:: Table of Contents
   :local:

Prerequisites
=============

1. :doc:`Install Nextstrain </install>` including the Nextstrain CLI. These instructions will install all of the software you need to complete this tutorial and others.

Setup
=====

Activate the ``nextstrain`` conda environment.

.. code-block::

    conda activate nextstrain

Download the Nextstrain Zika tutorial repository
================================================

We store our pathogen analyses in a version control repository, so we can easily track changes over time.
Download the `example Zika pathogen repository <https://github.com/nextstrain/zika-tutorial>`_ you're going to build.

.. code-block::

    $ git clone https://github.com/nextstrain/zika-tutorial
    Cloning into 'zika-tutorial'...
    [...more output...]

When it's done, you'll have a new directory called ``zika-tutorial/``.

Run the build
=============

Nextstrain builds use the :doc:`Augur bioinformatics toolkit <augur:index>` to subsample data, align sequences, build a phylogeny, estimate phylogeographic patterns, and save the results in a format suitable for :doc:`visualization with Auspice <auspice:index>`.

Run the build with the Nextstrain CLI.

.. code-block::

    $ nextstrain build --cpus 1 zika-tutorial/
    Building DAG of jobs...
    [...a lot of output...]

This should take just a few minutes to complete.
To save time, this tutorial build uses an example dataset which is much smaller than `our live Zika analysis <https://nextstrain.org/zika>`_.

Output files will be in the directories ``zika-tutorial/data/``, ``zika-tutorial/results/`` and ``zika-tutorial/auspice/``.

Visualize build results
=======================

View the build results using Nextstrain's visualizations.

.. code-block::

    $ nextstrain view zika-tutorial/auspice/
    ——————————————————————————————————————————————————————————————————————————————
        The following datasets should be available in a moment:
           • http://127.0.0.1:4000/local/zika
    ——————————————————————————————————————————————————————————————————————————————
    [...more output...]

`Open the link shown <http://127.0.0.1:4000/local/zika>`_ in your browser.

.. image :: ../images/zika_example.png
   :alt: Screenshot of Zika example dataset viewed in Nextstrain

Next steps
==========

* :doc:`Learn how to interpret Nextstrain's visualizations </learn/interpret/index>`
* :doc:`Explore Zika evolution in more detail </tutorials/zika>` or :doc:`explore Tuberculosis evolution </tutorials/tb_tutorial>`.
* Learn more about the CLI by running ``nextstrain --help`` and ``nextstrain <command> --help``.
* Explore the Nextstrain environment by running ad-hoc commands inside it using ``nextstrain shell zika/``.
