==========
Quickstart
==========

This guide uses the :doc:`Nextstrain command-line interface (CLI) <cli:index>` to help you get started running and viewing :doc:`the pathogen builds <augur:faq/what-is-a-build>` you see on `nextstrain.org <https://nextstrain.org>`_.
It assumes you are comfortable using the command line and installing software on your computer.
If you need help when following this guide, please reach out by `emailing us <mailto:hello@nextstrain.org?subject=Quickstart%20help>`_, or create a post at `discussion.nextstrain.org <https://discussion.nextstrain.org>`_.

When you're done following this guide, you will have built a local version of `our example Zika analysis <https://github.com/nextstrain/zika-tutorial>`_ and viewed the results on your computer.
You'll have a basic understanding of how to run builds for other pathogens and a foundation for understanding the Nextstrain ecosystem in more depth.

.. contents:: Table of Contents
   :local:

Setup
=====

:doc:`Install Nextstrain </install-nextstrain>` including the Nextstrain CLI.
These instructions will install all of the software you need to complete this quickstart and other tutorials.

If you've already installed Nextstrain, activate the Nextstrain environment.

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
