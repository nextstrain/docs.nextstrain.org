================================
Frequently Asked Questions (FAQ)
================================

.. contents:: Table of Contents
   :local:
   :depth: 2

Installation
============

There are many ways to install Nextstrain, and we aim to simplify the installation guide so it is easy to follow along. Here, you will find answers to some common questions about the installation process.


.. _whats-a-runtime:

What's a runtime?
-----------------

We use the term "runtime" (in the same sense as `runtime environments <https://en.wikipedia.org/wiki/Runtime_environment>`__) to refer to specific computing environments in which Nextstrain CLI expects to find and run other Nextstrain programs, like Augur and Auspice.
In turn, Nextstrain CLI provides a consistent set of commands to run and visualize Nextstrain pathogen builds regardless of the underlying runtime in use.
Together, this allows Nextstrain to be used across many different computing platforms and operating systems.
Not all Nextstrain CLI commands require a runtime, though usually one is required.

See Nextstrain CLI's :doc:`runtimes documentation <cli:runtimes/index>` for more information.


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

Should I use WSL or PowerShell on Windows?
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

.. _what-happened-to-the-intel-conda-recommendation:

What happened to the recommendation to use an Intel-based Conda installation?
-----------------------------------------------------------------------------

Background: computers with Apple silicon hardware have two options for Conda subdir: ``osx-arm64`` (native) and ``osx-64`` (Intel-based, requires Rosetta 2 emulation).

When Apple silicon was first released, few Conda packages supported ``osx-arm64``. This meant that the example ``conda create`` command provided in the Nextstrain docs would fail to resolve packages when using an ``osx-arm64`` Conda installation. We had suggested using an ``osx-64`` Conda installation as an easy workaround for most users, at the cost of not taking full advantage of the Apple silicon architecture.

Now that there is wide support for ``osx-arm64`` packages, we have removed the workaround.


.. _what-happened-to-the-native-runtime:

What happened to the "native" runtime?
----------------------------------------

The "native" runtime was **renamed to "ambient"** in Nextstrain CLI version 5.0.0, and we will use the new name going forwards.
The suitability of the "native" name had long been discussed within the Nextstrain team.

"Native" as a software term is typically used to describe software that can run without emulation, in other words optimized for your computer's processor.

The ambient runtime is native in that sense, but it puts all the software maintenance burden on the user. This means:

1. There is a lengthy setup process which requires installing external software (Conda). Additionally, there is no way for us to provide accurate setup steps for users who already have Conda installed, as there are various methods of installing Conda.
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
