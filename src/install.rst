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
Conda provides an appropriate version of Python required by all approaches to installing Nextstrain tools. Miniconda is the minimal installation of the command-line interface to Conda.

`Mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement for most ``conda`` functionality that implements a faster dependency solving algorithm in C++ and multithreaded downloads.
As a result, Mamba can install Conda packages much faster and more accurately than the original Conda installer.

`Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
When you use Docker to run Nextstrain components, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

Installation Steps
==================

These instructions will install the Nextstrain CLI and tools to run and view your own Nextstrain analyses. Configuration options vary by operating system.

.. tabs::

   .. group-tab:: macOS

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for Augur <augur:installation/installation>` and :doc:`install Auspice via npm <auspice:introduction/install>`.

      1. Install Miniconda:

         a. Go to the `installation page <https://docs.conda.io/en/latest/miniconda.html>`_.
         b. Scroll down to the **Latest Miniconda Installer Links** section and click the MacOSX platform link that ends with **pkg**.
         c. Open the downloaded file and follow through installation prompts.

      2. Open a terminal window.
      3. Install Mamba on the ``base`` Conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      4. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               .. warning::

                  If using a newer Mac with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), **Native** installation is recommended due to slowness with the Docker installation. `We are considering ways to improve this <https://github.com/nextstrain/docker-base/issues/35>`_.

               1. `Install Docker Desktop using the official guide <https://docs.docker.com/desktop/mac/install/>`_.
               2. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               3. Install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba install --yes nextstrain-cli

            .. group-tab:: Native

               .. warning::

                  If using a newer Mac with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), first run these commands to ensure Conda creates the environment with ``osx-64`` emulation:

                  .. code-block:: bash

                     # Create a new environment using Intel packages called base_osx-64
                     CONDA_SUBDIR=osx-64 conda create -n base_osx-64 python

                     # Activate new Intel-based environment
                     conda activate base_osx-64

                     # Ensure future Conda commands in this environment use Intel packages too.
                     conda config --env --set subdir osx-64

               1. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               2. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst

      5. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

   .. group-tab:: Windows

      .. note::

         Due to installation constraints, there is no way to use the native Nextstrain components on Windows directly. Follow steps for **WSL on Windows** if the native environment is desired.

      1. `Install Windows Subsystem for Linux (WSL) 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.

         .. note:: You may have to restart your machine when configuring WSL.

      2. `Install Docker Desktop with WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.
      3. Install Miniconda:

         a. Go to the `installation page <https://docs.conda.io/en/latest/miniconda.html>`_.
         b. Scroll down to the **Latest Miniconda Installer Links** section and click the Windows platform link relevant to your machine.
         c. Open the downloaded file and follow through installation prompts.

      4. Open an Anaconda PowerShell Prompt, which can be found in the Start menu. Note that you should not use the *administrator* prompt.
      5. Install Mamba on the ``base`` Conda environment:

         .. code-block:: powershell

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      6. Create a Conda environment named ``nextstrain``:

         .. include:: snippets/conda-create-powershell.rst

      7. Install the Nextstrain CLI:

         .. code-block:: powershell

            mamba install --yes nextstrain-cli

      8. Confirm that the installation worked.

         .. code-block:: powershell

            nextstrain check-setup --set-default

         The final output from the last command should look like this:

         .. code-block:: none

            Setting default environment to docker.

   .. group-tab:: WSL on Windows

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for Augur <augur:installation/installation>` and :doc:`install Auspice via npm <auspice:introduction/install>`.

      1. `Install Windows Subsystem for Linux (WSL) 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.

         .. note:: You may have to restart your machine when configuring WSL.

      2. Open a WSL terminal by running **wsl** from the Start menu.
      3. Install Miniconda:

         .. code-block:: bash

            wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
            bash Miniconda3-latest-Linux-x86_64.sh
            # follow through installation prompts
            rm Miniconda3-latest-Linux-x86_64.sh

      4. Install Mamba on the ``base`` Conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      5. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               1. On Windows, `install Docker Desktop with WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.

                  .. note:: Make sure to follow through the last step of enabling **WSL Integration**.

               2. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               3. Install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba install --yes nextstrain-cli

            .. group-tab:: Native

               1. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               2. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst

      6. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

   .. group-tab:: Ubuntu Linux

      .. note::

         If you are an experienced user, you can replace ``conda`` with ``pip`` but :doc:`note the extra installation steps for Augur <augur:installation/installation>` and :doc:`install Auspice via npm <auspice:introduction/install>`.

      1. Install Miniconda:

         .. code-block:: bash

            wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
            bash Miniconda3-latest-Linux-x86_64.sh
            # follow through installation prompts
            rm Miniconda3-latest-Linux-x86_64.sh

      2. Install Mamba on the ``base`` Conda environment:

         .. code-block:: bash

            conda install -n base -c conda-forge mamba --yes
            conda activate base

      3. Install the Nextstrain components. There are two options:

         .. tabs::

            .. group-tab:: Docker (recommended)

               .. note:: Steps for other Linux distributions (Debian, CentOS, RHEL, etc.) will be similar, though specific commands may vary slightly.

               1. Install Docker Engine using the standard Ubuntu package:

                  .. code-block:: bash

                     sudo apt install docker.io

                  .. note::

                     See `Docker's installation documentation <https://docs.docker.com/engine/install/ubuntu/>`__ for alternative installation methods.

               2. Add your user to the `docker` group:

                  .. code-block:: bash

                     sudo gpasswd --add $USER docker

               3. Restart your machine.
               4. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               5. Install the Nextstrain CLI:

                  .. code-block:: bash

                     mamba install --yes nextstrain-cli

            .. group-tab:: Native

               .. note:: Steps for other Linux distributions (Debian, CentOS, RHEL, etc.) should be identical or very similar.

               1. Create a Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               2. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst

      4. Confirm that the installation worked.

         .. code-block:: bash

            nextstrain check-setup --set-default

         The final output from the last command should look like this, where ``<option>`` is the option chosen in the previous step:

         .. code-block:: none

            Setting default environment to <option>.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.

Next, try :doc:`tutorials/running-a-workflow`.

.. note::

   Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the Conda environment with ``conda activate nextstrain``.

Update an existing installation
================================

Update the ``nextstrain`` Conda environment.

.. code-block:: bash

   mamba update -n base conda mamba
   conda activate nextstrain
   mamba update --all

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

Next steps
==========

With Nextstrain installed, try :doc:`tutorials/running-a-workflow` next.
