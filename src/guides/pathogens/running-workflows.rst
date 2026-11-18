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

      1. Run the default version of the workflow you have set up with :doc:`cli:commands/run`:

         .. code:: bash

            nextstrain run measles phylogenetic measles-analysis

         This will create the ``measles-analysis`` directory in your current directory.
         All outputs will be available in ``measles-analysis/results`` and ``measles-analysis/auspice``.

      2. The :doc:`cli:commands/run` command can also be used to run a different version of the workflow.
         Assuming you've already set up a different version of the measles repo from :ref:`managing-repo-setup`, run the ``repo-tutorial`` version with:

         .. code:: bash

            nextstrain run measles@repo-tutorial phylogenetic measles-branch-analysis

         This will create the ``measles-branch-analysis`` directory in your current directory.
         All outputs will be availalbe in ``measles-branch-analysis/results`` and ``measles-branch-analysis/auspice``.

   .. group-tab:: nextstrain build

      .. warning::

         Workflow runs with :doc:`cli:commands/build` will output results in the :term:`workflow directory`.
         Make sure to remove or move the outputs from any previous runs if you don't want the outputs don't get mixed.

      1. Run the default version of the workflow.

         From within the ``measles`` repository that you have set up, make sure you are on the ``main`` branch.

         .. code:: bash

            git switch main

         Then run the workflow with :doc:`cli:commands/build`:

         .. code:: bash

            nextstrain build phylogenetic

         All outputs will be available in ``phylogenetic/results`` and ``phylogenetic/auspice``.

      2. To run a different version of the workflow, first remove the outputs from the previous run:

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
When you run a workflow without any customizations, it will use the default configurations.
The default configuration is part of the pathogen repository source code as ``<workflow>/defaults/config.yaml``.
For example, within the `measles repository`_ you can find the default config for the phylogenetic workflow at ``phylogenetic/defaults/config.yaml``.

The configuration for a workflow run is output to ``results/run_config.yaml``, so you can copy and edit this file to customize the configuration for your analysis.

.. tabs::

   .. group-tab:: nextstrain run

      You can customize the workflow configuration for your analysis by adding a ``config.yaml`` file to your analysis directory.

      1. Manually create a new analysis directory:

         .. code:: bash

            mkdir custom-measles-analysis

      2. Copy the configuration file from the previous run to the new analysis directory:

         .. code:: bash

            cp measles-analysis/results/run_config.yaml custom-measles-analysis/config.yaml

      3. Open the ``custom-measles-analysis/config.yaml`` file in your preferred editor to customize it.
      4. Then run the workflow with your new analysis directory to use the custom config:

         .. code:: bash

            nextstrain run measles phylogenetic custom-measles-analysis

   .. group-tab:: nextstrain build

      You can customize the workflow configuration for your analysis by using a config file that must be located within the :term:`workflow directory`.
      We recommend a separate directory, e.g. ``build-configs``, for these custom config files so that they don't get overwritten by workflow outputs.

      1. Copy the configuration file from the previous run to the :term:`workflow directory`:

         .. code:: bash

            cp phylogenetic/results/run_config.yaml phylogenetic/build-configs/config.yaml

      2. Open the ``phylogenetic/build-configs/config.yaml`` file in your preferred editor to customize it.
      3. Then run the workflow with your custom config:

         .. code:: bash

            nextstrain build phylogenetic --configfile build-configs/config.yaml

         Note that the file path to the config file is relative to the workflow directory.

Customizing inputs
------------------

As introduced in the `Nextstrain blog <https://nextstrain.org/blog/2025-09-29-standardized-multiple-inputs>`_, Nextstrain maintained phylogenetic workflows are adopting standardized configurations for inputs.
The default configuration defines a list of ``inputs`` that usually points to the curated data that are produced by the pathogen's :term:`ingest workflow`.

You can use your custom config file to customize the inputs for your analysis:

1. Use ``additional_inputs`` to include inputs that would be merged with the default ``inputs``.
2. Use ``inputs`` to ignore the defaults and only include your own inputs.


Both config parameters support input files that are:

1. local files
2. remote files with an HTTPS URL
3. AWS S3 URIs, which requires AWS credentials

.. tabs::

   .. group-tab:: nextstrain run

      When inputs are local files, make sure they are located within your analysis directory.

      .. code::

         analysis-dir/
         ├── config.yaml
         └── data
             ├── metadata.tsv
             └── sequences.fasta

      Then in your ``config.yaml``, add the inputs with the file paths relative to the analysis directory:

      .. code:: yaml

         additional_inputs:
            - name: custom-inputs
              metadata: data/metadata.tsv
              sequences: data/sequences.fasta

   .. group-tab:: nextstrain build

      When inputs are local files, make sure why are located within the workflow directory.

      .. code::

         phylogenetics/
         └── data
             ├── metadata.tsv
             └── sequences.fasta

      Then in your ``config.yaml``, add the inputs with the file paths relative to the workflow directory:

      .. code:: yaml

         additional_inputs:
            - name: custom-inputs
              metadata: data/metadata.tsv
              sequences: data/sequences.fasta

Running workflows offline
=========================

Most steps in workflows should work offline with the exception of remote files that need to be downloaded.
The simplest method for preparing for offline workflow runs is to run the workflow when you still have internet connection to download the remote files ahead of time.

When running phylogenetic workflows with the standardized configurations for inputs, any remote files that are downloaded will be cached locally:

* With ``nextstrain run``, these are saved under ``<analysis-directory>/.snakemake/storage/``.
* With ``nextstrain build``, these are saved under ``<workflow>/.snakemake/storage/``.

These cached files are used in subsequent runs of the workflow if you are using the same analysis directory for ``nextstrain run`` or the same workflow directory for ``nextstrain build``
if one of the following is true:

1. Environment variable ``NEXTSTRAIN_REMOTE_FILES`` is set to a truthy value.
2. The config parameter ``use_remote_files`` is set to a truhy value.
3. When the workflow does not have a network connection.


.. _measles repository: https://github.com/nextstrain/measles
