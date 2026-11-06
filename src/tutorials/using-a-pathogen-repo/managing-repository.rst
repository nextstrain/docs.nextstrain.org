==============================
Managing a pathogen repository
==============================

This tutorial explains how to manage a Nextstrain :term:`pathogen repository` using either the :term:`Nextstrain CLI` or `Git <https://git-scm.com>`_.
It assumes you are comfortable using the command line and installing software on your computer.

.. contents:: Table of Contents
   :local:
   :depth: 2

Prerequisites
=============

1. :doc:`Install Nextstrain </install>`.
2. `Install Git <https://git-scm.com/install/>`_.


Setup
=====

.. tabs::

   .. group-tab:: Nexstrain CLI managed

      Set up the default `Zika pathogen repository <https://github.com/nextstrain/zika>`_ with the :doc:`cli:commands/setup` command:

      .. code:: console

         $ nextstrain setup zika --set-default
         Setting up zika@main…
         Extracted 94 files and directories to '/nextstrain/pathogens/zika/main=NVQWS3Q='.

         Checking setup…
         ✔ yes: downloaded
         ✔ yes: contains nextstrain-pathogen.yaml
         ✔ yes: nextstrain-pathogen.yaml declares `nextstrain run` compatibility
         ✔ yes: `nextstrain run` workflow 'ingest' exists
         ✔ yes: `nextstrain run` workflow 'phylogenetic' exists

         Setting pathogen default version to zika@main.

         All good!  Set up of zika@main complete.

      The output should show that the repository has two :term:`workflows <workflow>` compatible with :doc:`cli:commands/run`: ``ingest`` and ``phylogenetic``.

   .. group-tab:: Git managed

      Download the default `Zika pathogen repository <https://github.com/nextstrain/zika>`_ with:

      .. code:: console

         $ git clone https://github.com/nextstrain/zika
         Cloning into 'zika'...
         [...more output...]

      When it's done, you'll have a new directory called ``zika`` that contains all of the source code.


Run workflows
=============

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      Only workflows compatible with the :doc:`cli:commands/run` command are guaranteed to work:

      .. code:: bash

         nextstrain run zika phylogenetic zika-main

      The workflow will take a couple minutes to run and the workflow outputs will be available in the ``zika-main`` directory.
      You can view the produced dataset with:

      .. code:: bash

         nextstrain view zika-main

   .. group-tab:: Git managed

      By managing the pathogen repository with Git, you not confined to workflows that are compatible with ``nextstrain run``.

      First change to the ``zika`` directory:

      .. code:: bash

         cd zika

      Then you can run the workflow with :doc:`cli:commands/build`:

      .. code:: bash

         nextstrain build phylogenetic

      The workflow will take a couple minutes to run and the workflow outputs will be available in the ``phylogenetic`` directory.
      You can view the produced dataset with:

      .. code:: bash

         nextstrain view phylogenetic


Set up a different version
==========================

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      The :doc:`cli:commands/setup` command uses ``@<version>`` to point to a specific version of the pathogen repository.
      The ``version`` can point to a tag name, branch name, or a specific commit id.
      Instead of using the latest default version, point to a `branch in the same Zika repository <https://github.com/nextstrain/zika/tree/repo-tutorial>`_ with ``@repo-tutorial``:

      .. code:: bash

         nextstrain setup zika@repo-tutorial

      This should have similar outputs to when you set up the default version.

   .. group-tab:: Git managed

      Instead of using the latest default version, switch to a `branch in the same Zika repository <https://github.com/nextstrain/zika/tree/repo-tutorial>`_:

      .. code:: bash

         git switch repo-tutorial

      You can always check which version you are using by running ``git status``.

Check available versions
========================

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      The setup of the branch version does not interefere with the default version you set up previously.
      They are both available when you check available pathogens with the :doc:`cli:commands/version` command:

      .. code:: console

         $ nextstrain version --pathogens
         Nextstrain CLI X.Y.Z (standalone)

         Pathogens
           zika
             zika@main (default) {ingest, phylogenetic}
             zika@repo-tutorial

      This means you can easily manage multiple versions of the same pathogen repository.

   .. group-tab:: Git managed

      There is not one command to check all available versions since you can switch to any tag, branch, or specific commit in the repository.
      We recommend that you become familiar with `viewing the commit history <https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History>`_.

      For the purposes of this tutorial, you can see which branches you have set up with

      .. code:: bash

         git branch

Run a different version
=======================

.. tabs:

   .. group-tab:: Nextstrain CLI managed

      You can run the ``repo-tutorial`` version with a similar :doc:`cli:commands/run` command:

      .. code:: console

         $ nextstrain run zika@repo-tutorial phylogenetic zika-repo-tutorial

      The workflow will take a couple minutes to run and the workflow outputs will be available in the ``zika-repo-tutorial`` directory.
      You can view the produced dataset with:

      .. code:: bash

         nextstrain view zika-repo-tutorial

      Notice that this dataset has a different title than the default dataset.

   .. group-tab:: Git managed


Update
------

Since you just downloaded the repository, there are likely no updates when you try to update it with :doc:`cli:commands/update`.
To simulate the update process, we can force install an older version of the repository as the ``main`` version:

.. code:: console

   $ nextstrain setup zika@main=https://github.com/nextstrain/zika/zipball/89e230deab73a90065259d334415a4831ea66a18 --force
   Setting up zika@main…
   Removing existing setup '/Users/joverlee/.nextstrain/pathogens/zika/main=NVQWS3Q=' to start fresh…
   Extracted 100 files and directories to '/Users/joverlee/.nextstrain/pathogens/zika/main=NVQWS3Q='.

   Checking setup…
   ✔ yes: downloaded
   ✔ yes: contains nextstrain-pathogen.yaml
   ✘ no: nextstrain-pathogen.yaml declares `nextstrain run` compatibility
     (no workflows registered)

   Checks failed!  Setup is unlikely to be fully functional.

Then when you run the :doc:`cli:commands/update` command, it should update to the latest version that you had previously downloaded:

.. code:: console

   $ nextstrain update zika@main
   Checking for newer versions of Nextstrain CLI…

   Nextstrain CLI is up to date!

   Updating zika@main pathogen version…
   Updating 'zika@main' in-place…
   Removing existing setup '/Users/joverlee/.nextstrain/pathogens/zika/main=NVQWS3Q=' to start fresh…
   Extracted 94 files and directories to '/Users/joverlee/.nextstrain/pathogens/zika/main=NVQWS3Q='.
   Checking setup…
   ✔ yes: downloaded
   ✔ yes: contains nextstrain-pathogen.yaml
   ✔ yes: nextstrain-pathogen.yaml declares `nextstrain run` compatibility
   ✔ yes: `nextstrain run` workflow 'ingest' exists
   ✔ yes: `nextstrain run` workflow 'phylogenetic' exists
   Updated zika@main pathogen version!

   All updates successful!

Remove
------

We do not have a command to remove pathogen repositories yet.
Instead, you can manually remove the downloaded Zika repositories with these manual steps:

1. You can remove a specific version of the Zika repository, e.g. remove the ``repo-tutorial`` version with:

   .. code:: bash

      rm -rf ~/.nextstrain/pathogens/zika/repo-tutorial*

2. You can also remove all versions of the Zika repository with:

   .. code:: bash

      rm -rf ~/.nextstrain/pathogens/zika/




Run workflows
-------------

You can also run the branch version of the workflow, but beware that outputs can mix in the ``phylogenetic`` directory.

If you are using :ref:`the same directory <git-same-dir>` for different versions, then move the previous outputs to a different directory.

.. code:: bash

   mkdir ../zika-main
   mv phylogenetic/results ../zika-main
   mv phylogenetic/auspice ../zika-main

Then switch to the older version and run the workflow

.. code:: bash

   git switch repo-tutorial
   nextstrain build phylogenetic

Again, the workflow outputs will be available in the ``phylogenetic`` directory.

If you are using :ref:`a separate directory <git-separate-dir>` for different versions, then switch to that directory to run the workflow.

.. code:: bash

   cd ../zika-repo-tutorial
   git switch repo-tutorial
   nextstrain build phylogenetic
