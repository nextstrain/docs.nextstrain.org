==============================
Managing a pathogen repository
==============================

This guide explains how to manage a Nextstrain :term:`pathogen repository` using either the :term:`Nextstrain CLI` or `Git <https://git-scm.com>`_.

.. hint::

   If you are unsure which method to use, please refer to :ref:`choosing-pathogen-setup`

We will use the `measles repository`_ as an example of a Nextstrain pathogen repository throughout this guide.
This is a more complex repository than the `Zika tutorial repository`_ used in the earlier :doc:`/tutorials/running-a-phylogenetic-workflow` tutorial that is more representative of actively used Nextstrain pathogen repositories.

.. contents:: Table of Contents
   :local:
   :depth: 2

Set up the repository
=====================

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      Set up the default version with the :doc:`cli:commands/setup` command.
      For example, set up the `measles repository`_:

      .. code:: bash

         nextstrain setup measles --set-default

      The output should show whether the repository has :term:`workflows <workflow>` compatible with :doc:`cli:commands/run`.
      You should see that measles has three workflows that are compatible: ``ingest``, ``nextclade``, and ``phylogenetic``.

      The :doc:`cli:commands/setup` command can also be used to set up specific version of the repository.
      Use ``@<version>`` to point to a specific version of the pathogen repository.
      The ``<version>`` can point to a specific commit id, tag name, or branch name.
      Try pointing to a `branch in the same measles repository <https://github.com/nextstrain/measles/tree/repo-tutorial>`_ with ``@repo-tutorial``:

      .. code:: bash

         nextstrain setup measles@repo-tutorial

   .. group-tab:: Git managed

      Set up the default version with the `git clone <https://git-scm.com/docs/git-clone>`_ command.
      For example, set up the `measles repository`_ with:

      .. code:: bash

         git clone https://github.com/nextstrain/measles

      When it's done, you'll have a new directory called ``measles`` that contains all of the source code.

      If you would like to use a specific version, change into the ``measles`` directory and switch the version with the `git switch <https://git-scm.com/docs/git-switch>`_.
      Try switching to a `branch in the same measles repository <https://github.com/nextstrain/measles/tree/repo-tutorial>`_:

      .. code:: bash

         cd measles
         git switch repo-tutorial

      You can then check which version you are using with the `git status <https://git-scm.com/docs/git-status>`_ command.

      .. code:: console

         $ git status
         On branch repo-tutorial
         Your branch is up to date with 'origin/repo-tutorial'.

         nothing to commit, working tree clean

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
           measles
             measles@main (default) {ingest, phylogenetic, nextclade}
             measles@repo-tutorial {ingest, phylogenetic, nextclade}

      The version flagged as ``(default)`` is the version used if you do not specify ``@<version>``.
      The available workflows per version are listed in the curly brackets.

   .. group-tab:: Git managed

      There is not one single command to check all available versions since you can switch to any specific commit, tag, or branch in the repository.

      We recommend that you become familiar with the Git for

      1. `viewing the commit history <https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History>`_
      2. `basic tags <https://git-scm.com/book/en/v2/Git-Basics-Tagging>`_
      3. `branch management <https://git-scm.com/book/en/v2/Git-Branching-Branch-Management>`_

Update the repository
=====================

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      Update pathogen repositories with the :doc:`cli:commands/update` command.
      You can update any version that you have previously set up.

      For example, you can update the default version for measles with:

      .. code:: bash

         nextstrain update measles

      You can also update a specific version by adding ``@<version>``:

      .. code:: bash

         nextstrain update measles@repo-tutorial

   .. group-tab:: Git managed

      To update the ``main`` version, first make sure you are on the ``main`` branch

      .. code:: bash

         git switch main

      Then pull down the latest changes with

      .. code:: bash

         git pull

      Switch branches again to update the ``repo-tutorial`` version

      .. code:: bash

         git switch repo-tutorial

      Then pull down the latest changes with

      .. code:: bash

         git pull

      If you make changes in the source code that conflict with upstream changes, this can result in a merge conflict when you try to update the repository.
      If you run into an error, follow the `GitHub guide for resolving merge conflicts <https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/resolving-a-merge-conflict-using-the-command-line>`_.

Remove
======

.. tabs::

   .. group-tab:: Nextstrain CLI managed

      We do not have a command to remove pathogen repositories yet.
      Instead, you can manually remove the downloaded measles repository.

      You can remove a specific version of the measles repository, e.g. remove the ``repo-tutorial`` version with:

      .. code:: bash

         rm -rf ~/.nextstrain/pathogens/measles/repo-tutorial*

      You can also remove all versions of the measles repository with:

      .. code:: bash

         rm -rf ~/.nextstrain/pathogens/measles/

   .. group-tab:: Git managed

      .. warning::

         These commands will also delete any of your local changes on this branch!

      You can remove a specific branch version of the measles repository, e.g. remove the ``repo-tutorial`` branch version with:

      .. code:: bash

         git branch -D repo-tutorial

      The repository should always have the main default branch, so if you want to remove all versions of the measles repository, then remove the whole ``measles`` directory:

      .. code:: bash

         cd ../
         rm -rf measles

.. _measles repository: https://github.com/nextstrain/measles
.. _Zika tutorial repository: https://github.com/nextstrain/zika-tutorial
