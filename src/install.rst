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

    If you want to :doc:`contribute to the development of Nextstrain </guides/contribute/index>` or if you prefer to manage your own custom environment (e.g., a conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, and :doc:`Auspice <auspice:introduction/install>`.

.. contents:: Table of Contents
   :local:
   :depth: 1


Background
==========

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install Python and other software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).
Conda provides an appropriate version of Python required by all approaches to installing Nextstrain tools. Miniconda is the minimal installation of the command-line interface to conda.

`Mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement for most ``conda`` functionality that implements a faster dependency solving algorithm in C++ and multithreaded downloads.
As a result, mamba can install conda packages much faster and more accurately than the original conda installer.

`Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
When you use Docker to run Nextstrain components, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

Installation Steps
==================

These instructions will install the Nextstrain CLI and tools to run and view your own Nextstrain analyses. Configuration options vary by operating system.

.. tabs::

   .. group-tab:: macOS

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for augur <augur:installation/installation>` and :doc:`install auspice via npm <auspice:introduction/install>`.

      1. Install Miniconda:

         a. Go to the `installation page <https://docs.conda.io/en/latest/miniconda.html>`_.
         b. Scroll down to the **Latest Miniconda Installer Links** section and click the MacOSX platform link that ends with **pkg**.
         c. Open the downloaded file and follow through installation prompts.

      2. Open a terminal window.
      3. Install mamba on the ``base`` conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      4. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               .. warning::

                  If using a newer Mac with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), **Native** installation is recommended due to slowness with the Docker installation. `We are considering ways to improve this <https://github.com/nextstrain/docker-base/issues/35>`_.

               1. Install Docker Desktop using `the official guide <https://docs.docker.com/desktop/mac/install/>`_.
               2. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba create -n nextstrain -c bioconda nextstrain-cli --yes

               3. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain

            .. group-tab:: Native

               1. Create a conda environment named ``nextstrain`` and install all the necessary software using mamba:

                  .. code-block:: bash

                     mamba create -n nextstrain \
                       -c conda-forge -c bioconda \
                       nextstrain-cli augur auspice nextalign snakemake git \
                       --yes

               2. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain

      5. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

   .. group-tab:: Windows

      .. note::

         Due to installation constraints, there is no way to use the native Nextstrain components on Windows directly. Follow steps for **WSL on Windows** if the native environment is desired.

      1. Install Miniconda:

         a. Go to the `installation page <https://docs.conda.io/en/latest/miniconda.html>`_.
         b. Scroll down to the **Latest Miniconda Installer Links** section and click the Windows platform link relevant to your machine.
         c. Open the downloaded file and follow through installation prompts.

      2. Open an Anaconda PowerShell Prompt, which can be found in the Start menu.
      3. Install mamba on the ``base`` conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      4. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

         .. code-block:: none

            mamba create -n nextstrain -c bioconda nextstrain-cli --yes
            conda activate nextstrain

      5. Install the remaining Nextstrain components by `installing Docker Desktop with WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.

         .. note::

            You may have to restart your machine when configuring WSL (Windows Subsystem for Linux).
            If so, remember to open a new Anaconda PowerShell Prompt and run ``conda activate nextstrain`` before the next step.

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

      4. Install mamba on the ``base`` conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      5. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               1. On Windows, `install Docker Desktop for WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.

                  - Make sure to follow through the last step of enabling **WSL Integration**.

               2. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba create -n nextstrain -c bioconda nextstrain-cli --yes

               3. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain

            .. group-tab:: Native

               1. Create a conda environment named ``nextstrain`` and install all the necessary software using mamba:

                  .. code-block:: bash

                     mamba create -n nextstrain \
                       -c conda-forge -c bioconda \
                       nextstrain-cli augur auspice nextalign snakemake git \
                       --yes

               2. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain


      6. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

   .. group-tab:: Ubuntu Linux

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for augur <augur:installation/installation>` and :doc:`install auspice via npm <auspice:introduction/install>`.

      1. Install Miniconda:

         .. code-block:: bash

            wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
            bash Miniconda3-latest-Linux-x86_64.sh
            # follow through installation prompts
            rm Miniconda3-latest-Linux-x86_64.sh

      2. Install mamba on the ``base`` conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      3. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               1. Install Docker Engine for Ubuntu using the `convenience script <https://docs.docker.com/engine/install/ubuntu/#install-using-the-convenience-script>`_:

                  .. code-block:: bash

                     curl -fsSL https://get.docker.com -o get-docker.sh
                     sudo sh get-docker.sh
                     # follow through installation prompts
                     rm get-docker.sh

               2. Add your user to the `docker` group:

                  .. code-block:: bash

                     sudo usermod -aG docker $USER

               3. Restart your machine.
               4. Create a conda environment named ``nextstrain`` and install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba create -n nextstrain -c bioconda nextstrain-cli --yes

               5. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain

            .. group-tab:: Native

               1. Create a conda environment named ``nextstrain`` and install all the necessary software using mamba:

                  .. code-block:: bash

                     mamba create -n nextstrain \
                       -c conda-forge -c bioconda \
                       nextstrain-cli augur auspice nextalign snakemake git \
                       --yes

               2. Activate the conda environment:

                  .. code-block:: bash

                     conda activate nextstrain

      4. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.

Next, try :doc:`tutorials/running-a-workflow`.

.. note::

   Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the conda environment with ``conda activate nextstrain``.

Update an existing installation
================================

Update the `nextstrain` conda environment.

.. code-block:: bash

   mamba update -n base conda mamba
   conda activate nextstrain
   mamba update --all -c conda-forge -c bioconda

[Docker] Download the latest image with the Nextstrain CLI.

.. code-block:: bash

   nextstrain update

Troubleshoot a broken installation
==================================

If conda fails to install or update Nextstrain using the commands above, it's possible that conda itself is out-of-date or that conda cannot figure out how to resolve the environment's dependencies.
Try the following approaches, to fix these broken installations.

Remove your environment and start from scratch
----------------------------------------------

Starting from scratch often fixes problems with conda environments.
To start over with a new Nextstrain environment, delete your current environment.

.. code-block:: bash

    conda activate base
    conda env remove -n nextstrain

Then, repeat the installation instructions above, starting with the update of conda itself.

Next steps
==========

With Nextstrain installed, try :doc:`tutorials/running-a-workflow` next.
