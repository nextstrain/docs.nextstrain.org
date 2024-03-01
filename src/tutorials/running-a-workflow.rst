===========================
Running a pathogen workflow
===========================

This tutorial uses the :term:`Nextstrain CLI` to help you get started running :term:`pathogen workflows<workflow>` and viewing the :term:`datasets<dataset>` you see on `nextstrain.org <https://nextstrain.org>`_.
It assumes you are comfortable using the command line and installing software on your computer.
If you need help when following this tutorial, please create a post at `discussion.nextstrain.org <https://discussion.nextstrain.org>`_.

In this tutorial, you will run our `example Zika workflow <https://github.com/nextstrain/zika-tutorial>`_ and view the results on your computer.
You will have a basic understanding of how to run workflows for other pathogens and a foundation for understanding the Nextstrain ecosystem in more depth.

.. contents:: Table of Contents
   :local:

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`. These instructions will install all of the software you need to complete this tutorial and others.

Download the example Zika pathogen repository
=============================================

:term:`Pathogen workflows<workflow>` are stored in :term:`pathogen repositories<pathogen repository>` (version-controlled folders) to track changes over time. Download the `example Zika pathogen repository <https://github.com/nextstrain/zika-tutorial>`_.

.. code-block::

    $ git clone https://github.com/nextstrain/zika-tutorial
    Cloning into 'zika-tutorial'...
    [...more output...]

When it's done, you'll have a new directory called ``zika-tutorial/``.

Run the workflow
================

:term:`Pathogen workflows<workflow>` use the :term:`Augur` bioinformatics toolkit to subsample data, align sequences, build a phylogeny, estimate phylogeographic patterns, and save the results in a format suitable for visualization with :term:`Auspice`.

Run the workflow with the :term:`Nextstrain CLI`.

.. code-block::

    $ nextstrain build --cpus 1 zika-tutorial/
    Building DAG of jobs...
    [...a lot of output...]

This should take just a few minutes to complete.
To save time, this tutorial uses example data which is much smaller than `our live Zika analysis <https://nextstrain.org/zika>`_.

Output files will be in the directories ``zika-tutorial/data/``, ``zika-tutorial/results/`` and ``zika-tutorial/auspice/``.

Visualize results
=================

View the resulting :term:`dataset` using Nextstrain's visualizations.

.. code-block::

    $ nextstrain view zika-tutorial/auspice/
    ——————————————————————————————————————————————————————————————————————————————
        The following datasets should be available in a moment:
           • http://127.0.0.1:4000/zika
    ——————————————————————————————————————————————————————————————————————————————
    [...more output...]

Open the `dataset URL <http://127.0.0.1:4000/zika>`_ in your web browser.

.. image :: ../images/zika_example.png
   :alt: Screenshot of Zika example dataset viewed in Nextstrain

Next steps
==========

* :doc:`Learn how to interpret Nextstrain's visualizations </learn/interpret/index>`.
* :doc:`Learn how to create the workflow in this tutorial </tutorials/creating-a-workflow>`.
* Learn more about the CLI by running ``nextstrain --help`` and ``nextstrain <command> --help``.
* Explore the :term:`Nextstrain runtime<runtime>` by running ad-hoc commands inside it using ``nextstrain shell zika-tutorial/``.
