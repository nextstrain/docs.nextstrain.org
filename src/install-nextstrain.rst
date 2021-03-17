==================
Install Nextstrain
==================

Nextstrain is a collection of different tools including:

  * Augur: a bioinformatics toolkit for the analysis of pathogen genomes
  * Auspice: a tool for interactive visualization of pathogen evolution
  * Nextstrain command line interface (CLI): tools for management of analysis workflows and environments

The following instructions will install all of these tools.
For more details, :doc:`see the high level overview of these different components <learn/about-nextstrain>`.

.. contents:: Table of Contents
   :local:
   :depth: 1

.. note::

    If you want to contribute to the development of Nextstrain tools, see :doc:`the developer documentation for instructions to install these tools from source <guides/contribute/index>`.

    If you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, or :doc:`Auspice <auspice:introduction/install>`.

.. _install-with-conda:

Install Nextstrain in a Conda environment
=========================================

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).

.. note::

    If you use Microsoft Windows, `install the Windows Subsystem for Linux (WSL) <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
    Follow `instructions to open a new WSL window for your Linux distribution <https://docs.microsoft.com/en-us/windows/wsl/wsl-config>`_ and then run the following commands.

`Install Miniconda with Python 3 for your operating system <https://docs.conda.io/en/latest/miniconda.html>`_ and then update Conda to the latest version.

.. code-block:: bash

    conda activate base
    conda update conda

Create a Conda environment named ``nextstrain``.
This command will install Nextstrain and its dependencies.

.. code-block:: bash

    conda create -n nextstrain -c conda-forge -c bioconda nextstrain

Confirm that the installation worked.

.. code-block:: bash

    conda activate nextstrain
    nextstrain check-setup --set-default

The final output from the last command should look like this:

.. code-block:: bash

   Setting default environment to native.

Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the Nextstrain Conda environment with ``conda activate nextstrain``.

If you prefer to use Docker to manage your Nextstrain environment, follow the instructions below.
Otherwise, :doc:`check out the quickstart <tutorials/quickstart>` next.

.. _install-with-docker:

Configure Docker (optional)
===========================

`Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
When you use the Nextstrain CLI with Docker, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

`Follow Docker's installation guide <https://docs.docker.com/engine/install/>`_ for your operating system.
Note that for M1 Mac and Windows users, we recommend sticking with the Conda environment above.
Docker is not yet ready for widespread use on the M1 Mac.
Similarly, there are still significant obstacles to running Docker with Windows, as documented in `our issue tracking the problems <https://github.com/nextstrain/cli/issues/31>`_.

After installing and starting Docker, configure the Nextstrain CLI to use Docker as the default environment manager.

.. code-block:: bash

    nextstrain check-setup --set-default

The output of this last command should look like this:

.. code-block:: bash

    Setting default environment to docker.

Finally, download the latest Docker image for Nextstrain.

.. code-block:: bash

    nextstrain update

Next, :doc:`check out the quickstart <tutorials/quickstart>`.

Upgrade an existing installation
================================

Update the base Conda environment.

.. code-block:: bash

    conda activate base
    conda update conda

Update the Nextstrain environment.

.. code-block:: bash

    conda activate nextstrain
    conda update --all

If you are using the Docker image, download the latest version with the Nextstrain CLI.

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

Then, repeat :ref:`the installation instructions above <install-with-conda>`, starting with the update of Conda itself.

Use Mamba as an alternative to Conda's environment solver
---------------------------------------------------------

`Mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement for most ``conda`` functionality that implements a faster dependency solving algorithm in C++ and multithreaded downloads.
As a result, Mamba can install Conda packages much faster and more accurately than the original Conda installer.

To try it out, install Mamba.

.. code-block:: bash

    conda install -n base -c conda-forge mamba

Then, use Mamba to create the Nextstrain environment.

.. code-block:: bash

    mamba create -n nextstrain -c conda-forge -c bioconda nextstrain
