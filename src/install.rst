=====================
Installing Nextstrain
=====================

.. hint::

    Before installing, we recommend you read about the :doc:`parts of Nextstrain </learn/parts>`.

The following instructions describe how to install the full suite of Nextstrain's software tools, including:

  * Nextstrain CLI, for access to other tools and management of workflows
  * Augur, for bioinformatic analysis of pathogen genomes
  * Auspice, for interactive visualization of pathogen evolution

When completed, you'll be ready to run Nextstrain :term:`workflows <workflow>`.


.. contents:: Table of Contents
   :local:


Installation steps
==================

Steps vary by runtime option (Docker, Conda, ambient) and host interface (macOS, Windows (WSL), Windows (PowerShell), Linux).
For help choosing, refer to our :doc:`/reference/faq`, such as:

  * :ref:`whats-a-runtime`
  * :ref:`what-are-docker-conda-wsl-etc`
  * :ref:`choosing-a-runtime`
  * :ref:`what-happened-to-the-native-runtime`
  * :ref:`when-to-use-wsl`


Install Nextstrain CLI
----------------------

.. tabs::

   .. group-tab:: macOS

      In a Terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/mac | bash

      You can launch a Terminal by clicking the Launchpad icon in the Dock, typing ``terminal`` in the search field, and clicking Terminal.


   .. group-tab:: Windows (WSL)

      `Install Windows Subsystem for Linux (WSL) 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.
      You may have to restart your machine when configuring WSL.

      In a WSL terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

      You can launch a WSL terminal by clicking the Start menu, typing ``wsl``, and pressing enter.


   .. group-tab:: Windows (PowerShell)

      In a PowerShell terminal, run:

      .. code-block:: powershell

         Invoke-RestMethod https://nextstrain.org/cli/installer/windows | Invoke-Expression

      You can launch a PowerShell terminal by clicking the Start menu, typing ``powershell``, and pressing enter.
      Make sure to choose the item that is **not** marked "(Adminstrator)".


   .. group-tab:: Ubuntu Linux

      In a terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

      You can launch a terminal by clicking the "Show applications" icon in the Dock, typing ``terminal`` in the search field, and clicking Terminal.


Make sure to follow the installer's final instructions to setup your shell config.


Set up a Nextstrain runtime
---------------------------

.. tabs::

   .. group-tab:: Docker

      1. Install Docker on your computer.

         .. tabs::

            .. group-tab:: macOS

               `Install Docker Desktop for macOS <https://docs.docker.com/desktop/install/mac-install/>`_.


            .. group-tab:: Windows (WSL)

               `Install Docker Desktop for Windows`_ with the `WSL 2 backend`_.

               .. note::

                  Make sure to follow through to the **Enabling Docker support in WSL 2 distros** section and the last step of enabling **WSL Integration**.
                  If you forget to do this, ``docker`` won't work in the WSL terminal.

               .. include:: snippets/wsl-home-dir.rst


            .. group-tab:: Windows (PowerShell)

               `Install Windows Subsystem for Linux (WSL) 2`_.
               You may have to restart your machine when configuring WSL.

               `Install Docker Desktop for Windows <https://docs.docker.com/desktop/install/windows-install/>`_ with the `WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.


            .. group-tab:: Ubuntu Linux

               .. note:: Steps for other Linux distributions (Debian, CentOS, RHEL, etc.) will be similar, though specific commands may vary slightly.

               Install Docker Engine using the standard Ubuntu package:

                  .. code-block:: bash

                     sudo apt install docker.io

               or see `Docker Engine's installation documentation <https://docs.docker.com/engine/install/ubuntu/>`__ for alternative methods.

               Add your user to the ``docker`` group:

                  .. code-block:: bash

                     sudo gpasswd --add $USER docker

               Log out and back in again for the group change to take effect.


      2. Set up the runtime:

         .. code-block:: none

            nextstrain setup --set-default docker


   .. group-tab:: Conda

      .. tabs::

         .. group-tab:: macOS

            .. include:: snippets/nextstrain-setup-conda.rst

            .. note::

               On newer Macs with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), `Rosetta 2 <https://support.apple.com/en-us/HT211861>`__ is required for the Conda runtime.
               Most of the time, Rosetta 2 will already be enabled.
               If not, the installer will ask you to first enable Rosetta 2 and then retry the installation.


         .. group-tab:: Windows (WSL)

            .. include:: snippets/nextstrain-setup-conda.rst


         .. group-tab:: Windows (PowerShell)

            .. note::

               Due to installation constraints, there is no way to use Nextstrain's Conda runtime on Windows directly. Starting from the beginning, follow steps for **Windows (WSL)** if the Conda runtime is desired, or use the **Docker** runtime instead.


         .. group-tab:: Ubuntu Linux

            .. include:: snippets/nextstrain-setup-conda.rst


   .. group-tab:: Ambient (advanced)

      .. We use the phrase "custom Conda environment" to refer to a Conda environment managed by the user for use with the ambient runtime.

      The ambient runtime does not require a particular setup method; it will work as long as the programs you wish to use are available.

      The following describes how to accomplish this using a custom Conda environment as an example. You should be familiar with the `basics of Conda <https://conda.io/projects/conda/en/latest/user-guide/getting-started.html>`__ before proceeding.

      .. tabs::

         .. group-tab:: macOS

            .. warning::

               If step 2 fails, you might have an Apple silicon version of Conda installed. See :ref:`this FAQ section <why-conda-install-errors-on-apple-silicon>` for workarounds.

            .. include:: snippets/ambient-setup.rst


         .. group-tab:: Windows (WSL)

            .. include:: snippets/ambient-setup.rst


         .. group-tab:: Windows (PowerShell)

            .. note::

               Due to installation constraints, there is no way to use the ambient runtime on Windows directly. Starting from the beginning, follow steps for **Windows (WSL)** if the ambient runtime is desired, or use the **Docker** runtime instead.


         .. group-tab:: Ubuntu Linux

            .. include:: snippets/ambient-setup.rst



The final output from the last command should look like this, where ``<runtime>`` is the runtime option (e.g. Docker, Conda, or ambient) chosen in the first step:

.. code-block:: none

  Setting default environment to <runtime>.

  All good!  Set up of <runtime> complete.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.


Try running Augur and Auspice
-----------------------------

.. tabs::

   .. group-tab:: Docker

      1. Enter an interactive Nextstrain shell in the current directory (``.``).

         .. code-block:: bash

            nextstrain shell .

      2. Run Augur.

         .. code-block:: bash

            augur --help

      3. Run Auspice.

         .. code-block:: bash

            auspice --help

      4. Exit the Nextstrain shell.

         .. code-block:: bash

            exit


   .. group-tab:: Conda

      1. Enter an interactive Nextstrain shell in the current directory (``.``).

         .. code-block:: bash

            nextstrain shell .

      2. Run Augur.

         .. code-block:: bash

            augur --help

      3. Run Auspice.

         .. code-block:: bash

            auspice --help

      4. Exit the Nextstrain shell.

         .. code-block:: bash

            exit


   .. group-tab:: Ambient (advanced)

      .. note::

         This will vary depending on how your ambient runtime is set up.

      1. If using a custom Conda environment, activate it.

         .. code-block:: bash

            conda activate <your-environment-name>

      2. Run Augur.

         .. code-block:: bash

            augur --help

      3. Run Auspice.

         .. code-block:: bash

            auspice --help

      4. Deactivate the custom Conda environment.

         .. code-block:: bash

            conda deactivate


Next steps
==========

With Nextstrain installed, try :doc:`tutorials/running-a-phylogenetic-workflow` next.


Alternate installation methods
==============================

If you want to :doc:`contribute to the development of Nextstrain </guides/contribute/index>` or if you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, and :doc:`Auspice <auspice:introduction/install>`.


Managing an existing installation
=================================

See :doc:`guides/manage-installation` for steps to update, troubleshoot, or uninstall Nextstrain tools.
