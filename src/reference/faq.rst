================================
Frequently Asked Questions (FAQ)
================================

.. contents:: Table of Contents
   :local:
   :depth: 2

Installation
============

There are many ways to install Nextstrain, and we aim to simplify the installation guide so it is easy to follow along. Here, you will find answers to some common questions about the installation process.


.. _what-are-docker-conda-mamba-wsl-etc:

What are Docker, Conda, Mamba, WSL, etc.?
-----------------------------------------

`Docker <https://docker.com/>`_ is a container system available for all platforms.
When you use Docker to run Nextstrain components, you don’t need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`_.

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install Python and other software into controlled environments without disrupting other software you have installed (e.g., on your computer, your shared cluster, etc.).
Miniconda is the minimal installation of the ``conda`` command, the command-line interface to Conda.

`Mamba <https://github.com/mamba-org/mamba>`_ is a drop-in replacement for most ``conda`` functionality that provides faster installation times, especially for complex environments like the one Nextstrain requires.

`WSL <https://docs.microsoft.com/en-us/windows/wsl/about>`__ is Windows Subsystem for Linux, a full Linux environment integrated into Windows without the need for awkward virtual machines.
Nextstrain's installation guide works with WSL 2 but not WSL 1.


.. _choosing-a-runtime:

Should I choose the Docker or Ambient runtime?
----------------------------------------------

The two runtimes provide the same experience running Nextstrain workflows with ``nextstrain build`` (and most other ``nextstrain`` commands) but vary in installation and update methods and predictability/stability over time.

There's not one right answer for everyone or every situation.
That's why we provide both options (and will potentially provide more in the future).
The Nextstrain team uses both runtimes extensively.

Your preference is perhaps the best reason to choose one vs. the other.

   - If you have a preference for containers, then choose the Docker runtime.
   - If you have a preference for Conda, then choose the ambient runtime.
   - If you don't have a preference, choose the one you have the most past experience with.
   - If you have neither preference nor experience, we recommend choosing the Docker runtime because it has less to manage and is more predictable/stable over time.

You can also install and use both runtimes on the same computer, if you want to use them contextually.
For example, ``nextstrain`` commands let you select a different runtime than your default using command-line options (``--docker`` or ``--ambient``).

If you pick one and later realize you want to switch, you can go back and install the other and make it your default.


.. _when-to-use-wsl:

When should I use (or not use) WSL on Windows?
----------------------------------------------

All of our Windows installation guides actually require WSL; the difference between them is in the interface you ultimately use for Nextstrain.
This makes the choice mostly hinge on if you prefer a GNU/Linux `Bash shell <https://www.gnu.org/software/bash/manual/bash.html#What-is-Bash_003f>`__ interface or a Windows `PowerShell <https://docs.microsoft.com/en-us/powershell/scripting/discover-powershell>`__ interface for your command-line work.
If you don't have a preference (e.g. perhaps you're new to both), we suggest choosing the Bash shell.
Learning Bash will likely be useful in other work, as it is very widely used in bioinformatics and computing at large.

The other deciding factor is if you're unable to install Docker (e.g. for adminstrative or organizational reasons), then you'll need to use the **ambient** runtime with **WSL on Windows**.
The ambient runtime is not available without WSL.


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

.. _what-happened-to-the-native-runtime:

What happened to the ``native`` runtime?
----------------------------------------

Up until Nextstrain CLI version 5.0.0, the name of the ``native`` runtime has been debated internally. In CLI version 5.0.0, **it was renamed to** ``ambient`` and we will use the new name going forwards.

"Native" as a software term is typically used to describe software that can run without emulation, in other words optimized for your computer's processor.

The ``ambient`` runtime is "native" in that sense, but it puts all the software maintenance burden on the user. This means:

1. There is a lengthy setup process which requires installing external software (Conda, Mamba). Additionally, there is no way for us to provide accurate setup steps for users who already have Conda installed, as there are various methods of installing Conda.
2. It is up to you as the creator of the ``nextstrain`` Conda environment to know (1) how to activate it, (2) when to update it, and (3) how to update it.

So really, the ``ambient`` runtime is any environment that has been set up with all of the required software available on your local ``PATH``. We chose Conda in the installation instructions since some users may already be familiar with it, and it is simpler than using individual package managers for the various required software (e.g. ``pip``, ``npm``).

Most importantly, Nextstrain CLI version 5.0.0 provides a **new** ``conda`` **runtime that runs natively** without putting all of the software maintenance burden on users. This means the ``ambient`` runtime is no longer the only "native" runtime, and we will recommend new users to use the ``conda`` runtime instead of ``ambient``.

``ambient`` is still a good option for users who wish to customize their environment to include other software used in their workflows.

.. _new-conda-runtime-vs-old-native-runtime:

How is the new ``conda`` runtime different from the old ``native`` runtime?
---------------------------------------------------------------------------

Summary: ``conda``, like ``docker``, is fully managed by the Nextstrain CLI.

In ``docker``, the CLI manages versioning of the ``nextstrain/base`` Docker image, which comes packaged with common software tools used for Nextstrain-related analysis.

In ``conda``, the CLI manages the versioning of an isolated Conda environment separate from any existing Conda installation (if present). If you wish to use your existing Conda environment from the old ``native`` runtime or set up a new Conda environment, please refer to the ``ambient`` runtime usage instructions on the installation page.
