===============================
Running a phylogenetic workflow
===============================

This tutorial uses the :term:`Nextstrain CLI` to help you get started running :term:`phylogenetic workflows<phylogenetic workflow>` and viewing the :term:`datasets<phylogenetic dataset>` you see on `nextstrain.org <https://nextstrain.org>`_.
It assumes you are comfortable using the command line and installing software on your computer.
If you need help when following this tutorial, please create a post at `discussion.nextstrain.org <https://discussion.nextstrain.org>`_.

In this tutorial, you will run our `example Zika workflow <https://github.com/nextstrain/zika-tutorial>`_ and view the results on your computer.
You will have a basic understanding of how to run workflows for other pathogens and a foundation for understanding the Nextstrain ecosystem in more depth.

.. important::

   The first half of the tutorial teaches you how to run the workflow with :doc:`cli:commands/run` and the second half of the tutorial teaches you how to run it with :doc:`cli:commands/build`.
   We recommend that you become familiar with both methods as not all Nextstrain workflows are compatible with ``nextstrain run``.

.. contents:: Table of Contents
   :local:

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`. These instructions will install all of the software you need to complete this tutorial and others.

Run workflow with ``nextstrain run``
====================================

The :doc:`cli:commands/run` command is the newest command for running Nextstrain workflows.
Read our `introduction blog post <https://nextstrain.org/blog/2025-06-13-introducing-nextstrain-run>`_ for more details.

Set up the example Zika pathogen repository
-------------------------------------------

Set up the `example Zika pathogen repository <https://github.com/nextstrain/zika-tutorial>`_ with the :doc:`cli:commands/setup` command:

.. code-block:: console

    $ nextstrain setup zika-tutorial
    Setting up zika-tutorial@main...
    [...more output...]
    All good!  Set up of zika-tutorial@main complete.

When it's done, you can verify that ``zika-tutorial`` has been set up and see what :term:`workflows <workflow>` are available.
This example repository has a single ``phylogenetic`` workflow.

.. code-block:: console

   $ nextstrain version --pathogens
   Nextstrain CLI X.Y.Z (standalone)

   Pathogens
     zika-tutorial
       zika-tutorial@main (default) {phylogenetic}

Run the workflow
----------------

:term:`Phylogenetic workflows<phylogenetic workflow>` use the :term:`Augur` bioinformatics toolkit to subsample data, align sequences, build a phylogeny, estimate phylogeographic patterns, and save the results in a format suitable for visualization with :term:`Auspice`.

Run the workflow with the :doc:`cli:commands/run` command:

.. code-block:: console

    $ nextstrain run zika-tutorial phylogenetic zika-tutorial-analysis
    Running the 'phylogenetic' workflow for pathogen zika-tutorial@main
    [...a lot of output...]

This will automatically create the ``zika-tutorial-analysis`` :term:`analysis directory` in your current directory.
The workflow output files will be in ``zika-tutorial-analysis/results/`` and ``zika-tutorial-analysis/auspice/``.

This should take just a few minutes to complete.
To save time, this tutorial uses example data which is much smaller than `our live Zika analysis <https://nextstrain.org/zika>`_.

Visualize results
-----------------

View the resulting :term:`phylogenetic dataset` using Nextstrain's visualizations.

.. code-block:: console

    $ nextstrain view zika-tutorial-analysis
    ——————————————————————————————————————————————————————————————————————————————
        The following datasets should be available in a moment:
           • http://127.0.0.1:4000/zika
    ——————————————————————————————————————————————————————————————————————————————
    [...more output...]

Open the `dataset URL <http://127.0.0.1:4000/zika>`_ in your web browser.

.. image :: ../images/zika_example.png
   :alt: Screenshot of Zika example dataset viewed in Nextstrain

Run workflow with ``nextstrain build``
======================================

The :doc:`cli:commands/build` command is the traditional command used to run Nextstrain workflows.
It requires you to have direct access to the source code of the repository, so will require extra steps to set up.

Install Git
-----------

`Install Git <https://git-scm.com/install/>`_ if you don't already have it installed on your computer.

Download the example Zika repository
------------------------------------

:term:`Pathogen workflows<phylogenetic workflow>` are stored in :term:`pathogen repositories<pathogen repository>` (version-controlled folders) to track changes over time.
Download the `example Zika pathogen repository <https://github.com/nextstrain/zika-tutorial>`_ via Git:

.. code-block:: console

    $ git clone https://github.com/nextstrain/zika-tutorial
    Cloning into 'zika-tutorial'...
    [...more output...]

When it's done, you'll have a new directory called ``zika-tutorial/``.

Run the workflow
----------------

Run the workflow with the :doc:`cli:commands/build` command:

.. code-block:: console

    $ nextstrain build --cpus 1 zika-tutorial/
    Building DAG of jobs...
    [...a lot of output...]

As before, this should take just a few minutes to complete.
Output files will be in the directories ``zika-tutorial/data/``, ``zika-tutorial/results/`` and ``zika-tutorial/auspice/``.

Visualize results
-----------------

View the resulting :term:`phylogenetic dataset` using Nextstrain's visualizations.

.. code-block:: console

    $ nextstrain view zika-tutorial
    ——————————————————————————————————————————————————————————————————————————————
        The following datasets should be available in a moment:
           • http://127.0.0.1:4000/zika
    ——————————————————————————————————————————————————————————————————————————————
    [...more output...]


Open the `dataset URL <http://127.0.0.1:4000/zika>`_ in your web browser and you should see similar results as before.

Next steps
==========

* :doc:`Learn how to interpret Nextstrain's visualizations </learn/interpret/index>`.
* :doc:`Learn how to create the workflow in this tutorial </tutorials/creating-a-phylogenetic-workflow>`.
* Learn more about the CLI by running ``nextstrain --help`` and ``nextstrain <command> --help``.
* Explore the :term:`Nextstrain runtime<runtime>` by running ad-hoc commands inside it using ``nextstrain shell zika-tutorial/``.
