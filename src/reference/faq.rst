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

.. _check-existing-conda-installation:

Note for Apple silicon users with an existing Conda installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Conda is a popular tool, and you may already have it installed. If you are using a Mac computer with Apple silicon, the type of Conda installation determines whether you should run an additional step in Nextstrain installation.

1. Create and activate a new Conda environment with just Python installed:

   .. code-block:: bash

      mamba create -n tmp python --yes
      conda activate tmp

2. Check the type of Conda installation via Python:

   .. code-block:: bash

      python -c "import platform;print(platform.machine())"

   The output should be one of the following:

   - ``x86_64``: This means you have an Intel Conda installation. We recommend keeping this installation method and there is no extra step for Nextstrain installation.
   - ``arm64``: This means you have an Apple silicon Conda installation. You can choose to keep this installation to retain existing Conda environments, or to re-install with the Intel installer (note that you will have to re-create any existing environments). If you choose to keep this installation, please follow directions in the next section to properly install Nextstrain.

3. Remove the temporary Conda environment:

   .. code-block:: bash

      conda env remove -n tmp

.. _install-nextstrain-on-apple-silicon-conda:

Workaround for installing Nextstrain on an Apple silicon Conda installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For those who really want to use an Apple silicon (``arm64``) Conda installation, it is still possible to set up the ``nextstrain`` Conda environment by configuring it to run with emulation. Run this after setting up the empty ``nextstrain`` environment and before the ``mamba install`` command:

.. code-block:: bash

   conda config --env --set subdir osx-64

This will ensure that all commands in the active Conda environment are run using ``osx-64`` emulation, making it possible to install all the software required for Nextstrain to run.
