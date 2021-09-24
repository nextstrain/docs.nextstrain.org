=====================
Installing Nextstrain
=====================

.. hint::

    Before installing, we recommend you read about the :doc:`parts of Nextstrain </learn/parts>`.

The following instructions describe how to install Nextstrain's software tools with Conda or Docker, including:

  * Augur: a bioinformatics toolkit for the analysis of pathogen genomes
  * Auspice: a tool for interactive visualization of pathogen evolution
  * Nextstrain CLI: tools for management of analysis workflows and environments

.. note::

    If you want to :doc:`contribute to the development of Nextstrain </guides/contribute/index>` or if you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, or :doc:`Auspice <auspice:introduction/install>`.

.. contents:: Table of Contents
   :local:
   :depth: 1

Install Conda
=============

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install Python and other software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).
Conda provides an appropriate version of Python required by all approaches to installing Nextstrain tools.

.. note::

    If you use Microsoft Windows, `install the Windows Subsystem for Linux (WSL) <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
    Follow `instructions to open a new WSL window for your Linux distribution <https://docs.microsoft.com/en-us/windows/wsl/wsl-config>`_ and then run the following commands.

`Install Miniconda with Python 3 for your operating system <https://docs.conda.io/en/latest/miniconda.html>`_ and then update Conda to the latest version.

.. code-block:: bash

    conda update -n base conda

Install Nextstrain with Conda or Docker
=======================================

Next, decide whether you prefer to install Nextstrain with Conda or Docker.
We recommend Conda for M1 Mac and Windows users.
Docker is not yet ready for widespread use on the M1 Mac.
Similarly, there are still significant obstacles to running Docker with Windows, as documented in `our issue tracking the problems <https://github.com/nextstrain/cli/issues/31>`_.

.. tabs::

   .. group-tab:: Conda

      Create a Conda environment named ``nextstrain``.
      This command will install Nextstrain and its dependencies.

      .. code-block:: bash

         conda create -n nextstrain -c conda-forge -c bioconda \
           augur auspice nextstrain-cli nextalign snakemake awscli git pip

      Confirm that the installation worked.

      .. code-block:: bash

         conda activate nextstrain
         nextstrain check-setup --set-default

      The final output from the last command should look like this:

      .. code-block:: bash

         Setting default environment to native.

      Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the Nextstrain Conda environment with ``conda activate nextstrain``.
      Next, try :doc:`tutorials/quickstart`.

   .. group-tab:: Docker

    `Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
    When you use the Nextstrain CLI with Docker, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

    First, `follow Docker's installation guide <https://docs.docker.com/engine/install/>`_ for your operating system.
    After installing and starting Docker, create a Conda environment named ``nextstrain``.
    This command will install the Nextstrain CLI and Git (a dependency of subsequent tutorials).

    .. code-block:: bash

        conda create -n nextstrain -c conda-forge -c bioconda nextstrain-cli git

    Confirm that the installation worked and configure the CLI to use Docker as the default environment manager.

    .. code-block:: bash

        conda activate nextstrain
        nextstrain check-setup --set-default

    The final output from the last command should look like this:

    .. code-block:: bash

        Setting default environment to docker.

    Finally, download the latest Docker image for Nextstrain.

    .. code-block:: bash

        nextstrain update

    Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the Nextstrain Conda environment with ``conda activate nextstrain``.
    Next, try :doc:`tutorials/quickstart`.

Upgrade an existing installation
================================

.. tabs::

   .. group-tab:: Conda

      Update the base Conda environment.

      .. code-block:: bash

         conda update -n base conda

      Update the Nextstrain environment.

      .. code-block:: bash

         conda activate nextstrain
         conda update --all

   .. group-tab:: Docker

      Update the base Conda environment.

      .. code-block:: bash

         conda update -n base conda

      Update the Nextstrain CLI package.

      .. code-block:: bash

         conda activate nextstrain
         conda update nextstrain-cli

      Download the latest image with the Nextstrain CLI.

      .. code-block:: bash

         nextstrain update

Troubleshoot a broken installation
==================================

If Conda fails to install or update Nextstrain using the commands above, it's possible that Conda itself is out-of-date or that Conda cannot figure out how to resolve the environment's dependencies.
Try the following approaches, to fix these broken installations.

Remove your environment and start from scratch
----------------------------------------------

Starting from scratch often fixes problems with Conda environments.
To start over with a new Nextstrain environment, delete your current environment.

.. code-block:: bash

    conda activate base
    conda env remove -n nextstrain

Then, repeat the installation instructions above, starting with the update of Conda itself.

Use Mamba as an alternative to Conda's environment solver
---------------------------------------------------------

`Mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement for most ``conda`` functionality that implements a faster dependency solving algorithm in C++ and multithreaded downloads.
As a result, Mamba can install Conda packages much faster and more accurately than the original Conda installer.

To try it out, install Mamba.

.. code-block:: bash

    conda install -n base -c conda-forge mamba

Then, use Mamba to create the Nextstrain environment.

.. code-block:: bash

    mamba create -n nextstrain -c conda-forge -c bioconda \
      augur auspice nextstrain-cli nextalign snakemake awscli git pip

Similarly, use Mamba to update an existing Nextstrain environment to the latest versions of its tools.

.. code-block:: bash

    # Update Conda and Mamba.
    mamba update -n base conda mamba
    # Update tools in the Nextstrain environment.
    conda activate nextstrain
    mamba update --all -c conda-forge -c bioconda


Next steps
==========

With Nextstrain installed, try :doc:`tutorials/quickstart` next.
