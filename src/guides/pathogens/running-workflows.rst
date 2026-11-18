==========================
Running pathogen workflows
==========================

This is a general how-to guide for running pathogen :term:`workflows <workflow>` with :doc:`cli:commands/run` and :doc:`cli:commands/build`.
It assumes that you already know the basics of :doc:`./managing-repository`.

We will use the :term:`phylogenetic workflow` in the `measles repository`_ as an example workflow throughout this guide.
For workflow specific features, please refer to the individual pathogen repository documentation.

.. hint::

   If you are unsure which method to use, please refer to :ref:`choosing-run-method`

.. contents:: Table of Contents
   :local:
   :depth: 2


Running a workflow
==================

.. tabs::

   .. group-tab:: nextstrain run

      Run the default version of the workflow you have set up with :doc:`cli:commands/run`:

      .. code:: bash

         nextstrain run measles phylogenetic measles-analysis

      This will create the ``measles-analysis`` directory in your current directory.
      All outputs will be available in ``measles-analysis/results`` and ``measles-analysis/auspice``.

      The :doc:`cli:commands/run` command can also be used to run a different version of the workflow.
      Assuming you've already set up a different version of the measles repo from :ref:`managing-repo-setup`, run the ``repo-tutorial`` version with:

      .. code:: bash

         nextstrain run measles@repo-tutorial phylogenetic measles-branch-analysis

      This will create the ``measles-branch-analysis`` directory in your current directory.
      All outputs will be availalbe in ``measles-branch-analysis/results`` and ``measles-branch-analysis/auspice``.

   .. group-tab:: nextstrain build

      From within the ``measles`` repository that you have set up, make sure you are on the ``main`` branch.

      .. code:: bash

         git switch main

      Then run the workflow with :doc:`cli:commands/build`:

      .. code:: bash

         nextstrain build phylogenetic

      All outputs will be available in ``phylogenetic/results`` and ``phylogenetic/auspice``.

      .. warning::

         Workflow runs with :doc:`cli:commands/build` will output results in the :term:`workflow directory`.
         Make sure to remove or move the outputs from the previous run so the outputs don't get mixed.

      To run a different version of the workflow, first remove the outputs from the previous run:

      .. code:: bash

         rm -rf phylogenetic/results phylogenetic/auspice

      Switch to the different version, e.g. the ``repo-tutorial`` branch:

      .. code:: bash

         git switch repo-tutorial

      Then run the workflow with the same :doc:`cli:commands/build` command:

      .. code:: bash

         nextstrain build phylogenetic

Configuring a workflow
======================

Nextstrain maintained workflows usually have default configurations that are created for the Nextstrain builds.
You can view the default configuration that is part of the pathogen repository source code before running the workflow.
This is usually under ``<workflow>/defaults/config.yaml``, e.g. within the `measles repository`_ you can find ``phylogenetic/defaults/config.yaml``.

When you run a workflow without any additional configurations, it will use the default configurations.
A run configuration is output to ``results/run_config.yaml``, so you can copy and edit this file to customize the configuration for your analysis.

.. tabs::

   .. group-tab:: nextstrain run

      Manually create a new analysis directory:

      .. code:: bash

         mkdir custom-measles-analysis

      Then copy the configuration file from the previous run to the new analysis directory:

      .. code:: bash

         cp measles-analysis/results/run_config.yaml custom-measles-analysis/config.yaml

      Open the ``custom-measles-analysis/config.yaml`` file in your preferred editor to customize it.
      Then run the workflow with your custom config by pointing to the new analysis directory

      .. code:: bash

         nextstrain run measles phylogenetic custom-measles-analysis

   .. group-tab:: nextstrain build

      Copy the configuration file from the previous run to a new file within the :term:`workflow directory`.

      .. code:: bash

         cp phylogenetic/results/run_config.yaml phylogenetic/build-configs/custom-config.yaml

      Open the ``phylogenetic/build-configs/custom-config.yaml`` file in your preferred editor to customize it.
      Then run the workflow with your custom config by pointing to the new config file

      .. code:: bash

         nextstrain build phylogenetic --configfile build-configs/custom-config.yaml

Customizing inputs
------------------

XXXTODO: explain standardized inputs config


Running workflows offline
=========================

XXXTODO: explain offline options for inputs



.. _measles repository: https://github.com/nextstrain/measles
