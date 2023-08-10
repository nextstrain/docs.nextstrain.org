================================
Frequently Asked Questions (FAQ)
================================

.. contents:: Table of Contents
   :local:
   :depth: 2

Installation
============

There are many ways to install Nextstrain, and we aim to simplify the installation guide so it is easy to follow along. Here, you will find answers to some common questions about the installation process.


.. old anchors
.. _what-are-docker-conda-mamba-wsl-etc:

.. _what-are-docker-conda-wsl-etc:

What are Docker, Conda, WSL, etc.?
-----------------------------------------

`Docker <https://docker.com/>`_ is a container management system that allows you to run isolated software images without disrupting or *being* disrupted by other software you have installed (e.g., on your computer, your shared cluster, etc.).
When you use Nextstrain's Docker runtime, you need to install Docker yourself but don't need to manage any other Nextstrain software dependencies as validated versions are already bundled into `a container image by the Nextstrain team <https://github.com/nextstrain/docker-base/>`__.

`Conda <https://docs.conda.io/en/latest/>`_ is a package and environment management system that allows you to install Python and other software into controlled environments without disrupting other software you have installed.
Miniconda is the minimal installation of the ``conda`` command, the command-line interface to Conda.
When you use Nextstrain's Conda runtime, you don't need to install Conda yourself or manage any other Nextstrain software dependencies as validated versions are already locked into `a package by the Nextstrain team <https://github.com/nextstrain/conda-base/>`__.
When you use Nextstrain's ambient runtime, we provide an example of how to set it up using Conda.

`WSL <https://docs.microsoft.com/en-us/windows/wsl/about>`__ is Windows Subsystem for Linux, a full Linux environment integrated into Windows without the need for awkward virtual machines.
Nextstrain's installation guide works with WSL 2 but not WSL 1.


.. _choosing-a-runtime:

Should I choose the Docker, Conda, or ambient runtime?
------------------------------------------------------

The three runtimes provide the same experience running Nextstrain workflows with ``nextstrain build`` (and most other ``nextstrain`` commands) but vary in installation and update methods and predictability/stability over time.

There's not one right answer for everyone or every situation.
That's why we provide runtime options (and will potentially provide more in the future).
The Nextstrain team uses all runtimes extensively.

Your preference is perhaps the best reason to choose one vs. the other.

   - If you have a preference for containers, then choose the Docker runtime.
   - If you have a preference for Conda (or dispreference for containers), then choose the Conda runtime.
   - If you have a preference for managing software environments yourself, then choose the ambient runtime.
   - If you don't have a preference, choose the one you have the most past experience with.
   - If you have neither preference nor experience, we recommend choosing the Docker runtime because it is the most stable and reproducible over time.

You can also install and use multiple runtimes on the same computer, if you want to use them contextually.
For example, ``nextstrain`` commands let you select a different runtime than your default using command-line options (``--docker``, ``--conda``, or ``--ambient``).

If you pick one and later realize you want to switch, you can go back and install the other and make it your default.


.. _when-to-use-wsl:

Should I use PowerShell or WSL on Windows?
------------------------------------------

Both of our Windows installation guides require installation of WSL; the difference between them is in the interface you ultimately use for Nextstrain.
This makes the choice mostly hinge on what interface you prefer for your command-line work:

1. A GNU/Linux `Bash shell <https://www.gnu.org/software/bash/manual/bash.html#What-is-Bash_003f>`__ interface (choose **WSL**)
2. A Windows `PowerShell <https://docs.microsoft.com/en-us/powershell/scripting/discover-powershell>`__ interface (choose **PowerShell**)

If you don't have a preference (e.g. perhaps you're new to both), we suggest **WSL**.
Learning Bash will likely be useful in other work, as it is very widely used in bioinformatics and computing at large.

The other deciding factor is which runtime(s) you'd like to use. Under **PowerShell**, only the Docker runtime is available. If you're unable to install Docker (e.g. for administrative or organizational reasons), then you'll need to use **WSL** with one of the other runtimes.


.. old anchors
.. _why-intel-miniconda-installer-on-apple-silicon:

.. _why-conda-install-errors-on-apple-silicon:

Why do I get an error when installing to my Conda environment on a Mac computer with Apple silicon (e.g. M1)?
-------------------------------------------------------------------------------------------------------------

An example error:

.. code-block:: text
   :emphasize-lines: 9,10,11,12,13

   (your-environment-name) $ mamba install augur

   Looking for: ['augur']

   bioconda/osx-arm64

   …

   Could not solve for environment specs
   Encountered problems while solving:
     - nothing provides mafft needed by augur-10.0.0-py_0

   The environment can't be solved, aborting the operation

This happens when using an ARM64-based Conda installation on a `computer with Apple silicon <https://support.apple.com/en-us/HT211814>`__, but there are workarounds.

Apple silicon chips are great and efficient. They are based on a different chip architecture, ARM64/AArch64, and come with performance improvements compared to the x64-based Intel chips in older Macs.

However, many existing packages have not yet added support to run on these chips natively. An easy way to identify support on the `Bioconda packages page <https://anaconda.org/bioconda>`_ is to look for ``noarch`` or ``osx-arm64`` under the **Installers** section of a package. Without any of those, a package is not able to be installed natively on Apple silicon. This is the case for packages such as `MAFFT <https://anaconda.org/bioconda/mafft>`_ (a dependency of :term:`Augur`) and many other bioinformatics packages. For this reason, using an ARM64-based Conda installation for the average bioinformatics researcher can result in a difficult experience.

There are two ways to work around this:

1. Uninstall Conda, delete all existing environments, and re-install with an `Intel-based installer <https://docs.conda.io/en/latest/miniconda.html>`__. With an Intel-based installation, all environments are forced to use emulation.

   This provides easy compatibility with a broader set of bioinformatics packages, but comes at the cost of relatively longer run times for packages that have native ARM64 support.

2. Create a custom Conda environment that installs and runs packages under `Intel emulation <https://conda-forge.org/docs/user/tipsandtricks.html#installing-apple-intel-packages-on-apple-silicon>`__. Run this after setting up an **empty** Conda environment and before installing any packages to it:

   .. code-block:: bash

      conda config --env --set subdir osx-64

   This will ensure that all commands in the active Conda environment are run using Intel emulation, making it possible to install Nextstrain software such as Augur. You only need to run this once per Conda environment.

   .. warning::

      This should only be done on an empty Conda environment (otherwise you may encounter low-level errors) and does not automatically apply to other new or existing environments.

.. _what-happened-to-the-native-runtime:

What happened to the "native" runtime?
----------------------------------------

The "native" runtime was **renamed to "ambient"** in Nextstrain CLI version 5.0.0, and we will use the new name going forwards.
The suitability of the "native" name had long been discussed within the Nextstrain team.

"Native" as a software term is typically used to describe software that can run without emulation, in other words optimized for your computer's processor.

The ambient runtime is native in that sense, but it puts all the software maintenance burden on the user. This means:

1. There is a lengthy setup process which requires installing external software (Conda, Mamba). Additionally, there is no way for us to provide accurate setup steps for users who already have Conda installed, as there are various methods of installing Conda.
2. It is up to you as the creator of the ``nextstrain`` Conda environment to know (a) how to activate it, (b) when to update it, and (c) how to update it.

So really, the ambient runtime is any environment that has been set up with all of the required software available on your local ``PATH``. We chose Conda in the installation instructions since some users may already be familiar with it, and it is simpler than using individual package managers for the various required software (e.g. ``pip``, ``npm``).

Most importantly, Nextstrain CLI version 5.0.0 provides a **new Conda runtime that runs natively** without putting all of the software maintenance burden on users. This means the ambient runtime is no longer the only "native" runtime, and we will recommend new users to use the Conda runtime instead of ambient.

The ambient runtime is still a good option for users who wish to customize their environment to include other software used in their workflows.

.. _new-conda-runtime-vs-old-native-runtime:

How is the new Conda runtime different from the old "native" runtime?
---------------------------------------------------------------------------

The Conda runtime, like the Docker runtime, is fully managed by the Nextstrain CLI.
The CLI manages the versioning of an isolated Conda environment separate from any existing Conda installation (if present).
It ensures all the software tools used for Nextstrain-related analysis are available and handles updates to them via the ``nextstrain update`` command (like the Docker runtime).

If you wish to use your existing ``nextstrain`` Conda environment from the previously-named native runtime or set up a new Conda environment yourself, please refer to the ambient runtime usage instructions on the installation page.
