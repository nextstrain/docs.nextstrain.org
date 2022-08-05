================================
Frequently Asked Questions (FAQ)
================================

.. TODO: Add a table of contents once there are more sections. Doesn't seem necessary at the time of writing.

Installation
============

There are many ways to install Nextstrain, and we aim to simplify the installation guide so it is easy to follow along. Here, you will find answers to some common questions about the installation process.

.. _why-intel-miniconda-installer-on-apple-silicon:

Why recommend the Intel Miniconda installer for Mac computers with Apple silicon (e.g. M1)?
-------------------------------------------------------------------------------------------

.. note::

   `How to tell if your Mac has an Apple silicon chip <https://support.apple.com/en-us/HT211814>`_

Apple silicon chips are great and efficient. However, many existing packages have not yet added support to run on these chips natively. An easy way to identify support on the `Bioconda packages page <https://anaconda.org/bioconda>`_ is to look for ``noarch`` or ``osx-arm64`` under the **Installers** section of a package. Without any of those, a package is not able to be installed natively on Apple silicon. This is the case for packages such as `MAFFT <https://anaconda.org/bioconda/mafft>`_ (a dependency of :term:`Augur`) and many other bioinformatics packages. For this reason, using an Apple silicon Miniconda installation for the average bioinformatics researcher can result in a difficult experience. To circumvent this, one may enable ``osx-64`` emulation using the ``subdir`` config on each Conda environment, but it is easier to install with emulation by default.

For those who really want to use the ``arm64`` Miniconda installer, it is still possible to set up the ``nextstrain`` Conda environment by configuring it to run with emulation. Run this after setting up the empty Conda environment and before the ``mamba install`` command:

.. code-block:: bash

   conda config --env --set subdir osx-64

This will ensure that all commands in the active Conda environment are run using ``osx-64`` emulation, making it possible to install all the software required for Nextstrain to run.
