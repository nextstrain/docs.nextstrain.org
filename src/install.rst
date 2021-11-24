=====================
Installing Nextstrain
=====================

.. hint::

    Before installing, we recommend you read about the :doc:`parts of Nextstrain </learn/parts>`.

The following instructions describe how to install Nextstrain's software tools, including:

  * Augur: a bioinformatics toolkit for the analysis of pathogen genomes
  * Auspice: a tool for interactive visualization of pathogen evolution
  * Nextstrain CLI: tools for management of analysis workflows and environments

.. note::

    If you want to :doc:`contribute to the development of Nextstrain </guides/contribute/index>` or if you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, and :doc:`Auspice <auspice:introduction/install>`.

.. contents:: Table of Contents
   :local:
   :depth: 1


Background
==========

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install Python and other software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).
Conda provides an appropriate version of Python required by all approaches to installing Nextstrain tools.

`Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
When you use the Docker build/view environment, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

Installation Steps
==================

These instructions will install the Nextstrain CLI and tools to run and view your own Nextstrain analyses. Configuration options vary by operating system.

.. tabs::

   .. group-tab:: macOS

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for augur <augur:installation/installation>` and :doc:`install auspice via npm <auspice:introduction/install>`.

      1. Install `Anaconda or Miniconda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html>`_.
         Miniconda is sufficient for this guide.
      2. Open a terminal window.
      3. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

         .. code-block:: bash

            conda create -n nextstrain -c bioconda nextstrain-cli --yes
            conda activate nextstrain

      4. Install the remaining Nextstrain components. There are two options:

         a. Docker (recommended) – install Docker Desktop using `the official guide <https://docs.docker.com/desktop/mac/install/>`_.
         b. Native – install all the necessary software using conda:

            .. code-block:: bash

               conda install -c conda-forge -c bioconda augur auspice snakemake --yes

      5. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

   .. group-tab:: Windows

      .. note::

         Due to installation constraints, there is no way to use the native build/view environment on Windows directly. Follow steps for **WSL on Windows** if the native environment is desired.

      1. Install `Anaconda or Miniconda <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html>`_.
         Miniconda is sufficient for this guide.
      2. Install Visual C++ build tools following `this guide <https://stackoverflow.com/a/64262038>`_.

         - This is necessary for a dependency of Nextstrain CLI and `we are investigating options to eliminate this step <https://github.com/nextstrain/cli/issues/31#issuecomment-970641263>`_.

      3. Open an Anaconda Prompt, which can be found in the Start menu.
      4. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

         .. code-block:: none

            conda create -n nextstrain -c bioconda nextstrain-cli --yes
            conda activate nextstrain

      5. Install the remaining Nextstrain components by `installing Docker Desktop with WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.
      6. Confirm that the installation worked.

         .. code-block:: none

            nextstrain check-setup --set-default

         The final output from the last command should look like this:

         .. code-block:: none

            Setting default environment to docker.

   .. group-tab:: WSL on Windows

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for augur <augur:installation/installation>` and :doc:`install auspice via npm <auspice:introduction/install>`.

      1. `Install WSL 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.
      2. Open a WSL terminal by running **wsl** from the Start menu.
      3. Install Miniconda:

         .. code-block:: bash

            wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
            bash Miniconda3-latest-Linux-x86_64.sh
            # follow through installation prompts
            rm Miniconda3-latest-Linux-x86_64.sh

      4. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

         .. code-block:: bash

            conda create -n nextstrain -c bioconda nextstrain-cli --yes
            conda activate nextstrain

      5. Install the remaining Nextstrain components. There are two options:

         a. Docker (recommended) – on Windows, `install Docker Desktop for WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.

            - Make sure to follow through the last step of enabling **WSL Integration**.

         b. Native – install all the necessary software using conda:

            .. code-block:: bash

               conda install -c conda-forge -c bioconda augur auspice snakemake --yes

      6. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.

Next, try :doc:`tutorials/quickstart`.

.. note::

   Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the conda environment with ``conda activate nextstrain``.

Update an existing installation
================================

Update the `nextstrain` conda environment.

.. code-block:: bash

   conda activate nextstrain
   conda update --all

[Docker] Download the latest image with the Nextstrain CLI.

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
