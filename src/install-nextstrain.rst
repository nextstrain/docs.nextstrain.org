==================
Install Nextstrain
==================

Nextstrain is a collection of different tools including:

  * Augur: a bioinformatics toolkit for the analysis of pathogen genomes
  * Auspice: a tool for interactive visualization of pathogen evolution
  * Nextstrain command line interface (CLI): tools for management of analysis workflows and environments

For more details, :doc:`see the high level overview of these different components <learn/about-nextstrain>`.

.. note::

    If you want to contribute to the development of Nextstrain tools, see :doc:`the developer documentation for instructions to install these tools from source <guides/contribute/index>`.

    If you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, or :doc:`Auspice <auspice:introduction/install>`.

Install Nextstrain in a Conda environment
=========================================

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).

.. note::

    If you do not want to manage your own software environment or if you need to run your analyses in a containerized environment (e.g., on a cloud compute platform), follow :ref:`the instructions to configure the Nextstrain Docker image <install-with-docker>`, after this initial installation.

`Install Miniconda with Python 3 for your operating system <https://docs.conda.io/en/latest/miniconda.html>`_.
Setup Conda channels for Nextstrain and its dependencies.

.. code-block:: bash

    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge

Create a Conda environment for Nextstrain and install Nextstrain and its dependencies.

.. code-block:: bash

    conda create -n nextstrain nextstrain-cli augur nextalign nodejs
    conda activate nextstrain
    npm install --global auspice

Confirm that the installation worked and tell the Nextstrain CLI to use this environment by default.

.. code-block:: bash

    nextstrain check-setup --set-default

Congratulations!
You have successfully installed Nextstrain.
Activate this Conda environment with ``conda activate nextstrain`` any time you need to run an analysis.

If you prefer to use Docker to manage your Nextstrain environment, follow the instructions below.
Otherwise, :doc:`check out the quickstart <tutorials/quickstart>` next.

.. _install-with-docker:

Configure Docker (optional)
===========================

`Docker <https://docker.com/>`_ is a container system freely-available for all platforms.
When you use the Nextstrain CLI with Docker, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

Linux
-----

Install Docker with the standard package manager.
For example, on Ubuntu, you can install Docker with ``sudo apt install docker.io``.

Mac OS
------

Download and install `Docker Desktop <https://www.docker.com/products/docker-desktop>`_, also known previously as "Docker for Mac".
Note that if you have a M1 Mac, Docker is not yet ready for widespread use, and so we recommend sticking with the Conda environment above.

Windows
-------

There are still significant obstacles to running Docker with Windows, as documented in `our issue tracking the problems <https://github.com/nextstrain/cli/issues/31>`_.
However, if you have access to `WSL2 <https://docs.microsoft.com/en-us/windows/wsl/wsl2-index>`_, you should be able to use Docker inside it by following the Linux install instructions.
Alternatively, you can use the Conda environment above or AWS Batch.

After installing and starting Docker, configure the Nextstrain CLI to use Docker as the default environment manager.

.. code-block:: bash

    nextstrain check-setup --set-default

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
    npm update --global auspice

If you are using the Docker image, download the latest version with the Nextstrain CLI.

.. code-block:: bash

    nextstrain update
