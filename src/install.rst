=====================
Installing Nextstrain
=====================

.. hint::

    Before installing, we recommend you read about the :doc:`parts of Nextstrain </learn/parts>`.

The following instructions describe how to install the full suite of Nextstrain's software tools, including:

  * Augur, for bioinformatic analysis of pathogen genomes
  * Auspice, for interactive visualization of pathogen evolution
  * Nextstrain CLI, for management of analysis workflows and environments

When completed, you'll be ready to run Nextstrain :term:`workflows <workflow>`.

Installation steps
==================

Steps vary by runtime option (Docker, Conda, ambient) and operating system (macOS, Windows, WSL on Windows, Linux).
For help choosing, refer to our :doc:`/reference/faq`, such as:

  * :ref:`what-are-docker-conda-mamba-wsl-etc`
  * :ref:`choosing-a-runtime`
  * :ref:`what-happened-to-the-native-runtime`
  * :ref:`when-to-use-wsl`

First, install Nextstrain CLI.

.. tabs::

   .. group-tab:: macOS

      In a Terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/mac | bash

      You can launch a Terminal by clicking the Launchpad icon in the Dock, typing ``terminal`` in the search field, and clicking Terminal.

      .. note::

         On newer Macs with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), `Rosetta 2 <https://support.apple.com/en-us/HT211861>`__ is required for both Nextstrain CLI itself and our runtimes.
         Most of the time, Rosetta 2 will already be enabled.
         If not, the installer will ask you to first enable Rosetta 2 and then retry the installation.

   .. group-tab:: Windows

      In a PowerShell terminal, run:

      .. code-block:: powershell

         Invoke-RestMethod https://nextstrain.org/cli/installer/windows | Invoke-Expression

      You can launch a PowerShell terminal by clicking the Start menu, typing ``powershell``, and pressing enter.
      Make sure to choose the item that is **not** marked "(Adminstrator)".


   .. group-tab:: WSL on Windows

      `Install Windows Subsystem for Linux (WSL) 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.
      You may have to restart your machine when configuring WSL.

      In a WSL terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

      You can launch a WSL terminal by clicking the Start menu, typing ``wsl``, and pressing enter.


   .. group-tab:: Ubuntu Linux

      In a terminal, run:

      .. code-block:: bash

         curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

      You can launch a terminal by clicking the "Show applications" icon in the Dock, typing ``terminal`` in the search field, and clicking Terminal.


Make sure to follow the installer's final instructions to setup your shell config.


Then, install a Nextstrain runtime.

.. tabs::

   .. group-tab:: Docker

      1. Install Docker on your computer.

         .. tabs::

            .. group-tab:: macOS

               `Install Docker Desktop for macOS <https://docs.docker.com/desktop/install/mac-install/>`_.


            .. group-tab:: Windows

               `Install Windows Subsystem for Linux (WSL) 2`_.
               You may have to restart your machine when configuring WSL.

               `Install Docker Desktop for Windows <https://docs.docker.com/desktop/install/windows-install/>`_ with the `WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.


            .. group-tab:: WSL on Windows

               `Install Docker Desktop for Windows`_ with the `WSL 2 backend`_.

               .. note::

                  Make sure to follow through to the **Enabling Docker support in WSL 2 distros** section and the last step of enabling **WSL Integration**.
                  If you forget to do this, ``docker`` won't work in the WSL terminal.

               .. include:: snippets/wsl-home-dir.rst


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

         .. group-tab:: Windows

            .. note::

               Due to installation constraints, there is no way to use Nextstrain's Conda runtime on Windows directly. Starting from the beginning, follow steps for **WSL on Windows** if the Conda runtime is desired, or use the **Docker** runtime instead.

         .. group-tab:: WSL on Windows

            .. include:: snippets/nextstrain-setup-conda.rst

         .. group-tab:: Ubuntu Linux

            .. include:: snippets/nextstrain-setup-conda.rst

   .. group-tab:: Ambient

      .. We use the phrase "custom Conda environment" to refer to the Conda environment managed by the user for use with the ambient runtime.

      .. note:: The ambient runtime does not require a particular installation method; it will work as long as the programs required by Nextstrain are available.
         The following describes how to accomplish this using a custom Conda environment as an example.

         If you already have Conda or Mamba installed and use it for other projects, you may need to adjust the instructions below.

      1. Install the necessary programs into a custom Conda environment you manage.

         .. tabs::

            .. group-tab:: macOS

               1. Install Miniconda:

                  .. The installer link is taken from https://docs.conda.io/en/latest/miniconda.html.

                  a. `Download the installer <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_.

                     .. note::

                           This is the Intel x86 64-bit installer, :ref:`which we recommend even for Mac computers with Apple silicon (e.g. M1) <why-intel-miniconda-installer-on-apple-silicon>`.

                  b. Open the downloaded file and follow through installation prompts.

               2. Open a new terminal window.
               3. Install Mamba on the ``base`` Conda environment:

                  .. code-block:: bash

                     conda install -n base -c conda-forge mamba --yes
                     conda activate base

               4. Create a custom Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               5. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst


            .. group-tab:: Windows

               .. note::

                  Due to installation constraints, there is no way to use the ambient runtime on Windows directly. Starting from the beginning, follow steps for **WSL on Windows** if the ambient runtime is desired, or use the **Docker** runtime instead.


            .. group-tab:: WSL on Windows

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

               3. Create a custom Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               4. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst

               .. include:: snippets/wsl-home-dir.rst


            .. group-tab:: Ubuntu Linux

               .. note:: Steps for other Linux distributions (Debian, CentOS, RHEL, etc.) should be identical or very similar.

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

               3. Create a custom Conda environment named ``nextstrain``:

                  .. include:: snippets/conda-create-bash.rst

               4. Install all the necessary software:

                  .. include:: snippets/conda-install-full-bash.rst


      2. Set up the runtime:

         .. code-block:: none

            nextstrain setup --set-default ambient


      .. admonition:: For ambient runtime installs
         :class: hint

         Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the custom Conda environment with ``conda activate nextstrain``.



The final output from the last command should look like this, where ``<runtime>`` is the runtime option (e.g. Docker, Conda, or ambient) chosen in the first step:

.. code-block:: none

  Setting default environment to <runtime>.

  All good!  Set up of <runtime> complete.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.

Next, try :doc:`tutorials/running-a-workflow`.


Update an existing installation
================================

.. tabs::

   .. group-tab:: Docker

      Update the Docker runtime:

      .. code-block:: bash

         nextstrain update docker

      If the output notes that an update of the Nextstrain CLI itself is available, run the suggested command (after optionally reviewing the release notes).


   .. group-tab:: Conda

      Update the Conda runtime:

      .. code-block:: bash

         nextstrain update conda

      If the output notes that an update of the Nextstrain CLI itself is available, run the suggested command (after optionally reviewing the release notes).


   .. group-tab:: Ambient

      Update the ``nextstrain`` custom Conda environment.

      .. code-block:: bash

         mamba update -n base conda mamba
         conda activate nextstrain
         mamba update --all
         nextstrain check-setup ambient

      If the output of the final command notes that an update of the Nextstrain CLI itself is available, run the suggested command (after optionally reviewing the release notes).


Troubleshoot a broken installation
==================================

.. tabs::

   .. group-tab:: Docker

      Running ``nextstrain check-setup docker`` will also report potential issues.
      Make sure there are no errors or warnings reported.

      The Docker runtime requires that the Docker service is running on your computer behind the scenes.
      If you see a message like::

         Cannot connect to the Docker daemon at […]. Is the docker daemon running?

      Then it is likely that the Docker service is not running.
      On macOS and Windows, try quitting Docker Desktop (if it's open) and restarting it.
      On Linux, try running ``sudo systemctl restart docker``.


   .. group-tab:: Conda

      Running ``nextstrain check-setup conda`` will report potential issues.
      Make sure there are no errors or warnings reported.

      You can forcibly setup the Conda runtime again by running:

      .. code-block:: bash

         nextstrain setup --force conda

      This should rarely be necessary, but may help if you find yourself with a broken runtime.


   .. group-tab:: Ambient

      Running ``nextstrain check-setup ambient`` will report potential issues.
      Make sure there are no errors or warnings reported.

      Ensure that you've activated your custom Conda environment with ``conda activate nextstrain``.

      If Conda fails to install or update Nextstrain using the commands in the other sections above, it's possible that Conda itself is out-of-date or that Conda cannot figure out how to resolve the environment's dependencies.
      Starting from scratch often fixes problems with Conda environments.
      To start over with a new Nextstrain environment, delete your current environment.

      .. code-block:: bash

          conda activate base
          conda env remove -n nextstrain

      Then, repeat the installation instructions above, starting with the update of Conda itself.

If you the above isn't sufficient and you need more help troubleshooting, please post to our `discussion forum <https://discussion.nextstrain.org/c/help-and-getting-started/6>`__ where members of the community and the Nextstrain team can help out.

Alternate installation methods
==============================

If you want to :doc:`contribute to the development of Nextstrain </guides/contribute/index>` or if you prefer to manage your own custom environment (e.g., a Conda environment, Docker image, environment modules on a cluster, etc.), see the individual installation documentation for :doc:`Nextstrain CLI <cli:installation>`, :doc:`Augur <augur:installation/installation>`, and :doc:`Auspice <auspice:introduction/install>`.

Uninstall
=========

We do not have an automated uninstall process currently.
Instead, follow these manual steps:

   1. If the directory :file:`~/.nextstrain` exists, remove it.
   2. If using the Docker runtime, remove all ``nextstrain/…`` Docker images::

         docker image rm $(docker image ls -q "nextstrain/*")

      Optionally, uninstall Docker if only used for Nextstrain.
   3. If using the ambient runtime, remove the ``nextstrain`` custom Conda environment::

         conda env remove -n nextstrain

      Optionally, uninstall Conda if only used for Nextstrain.
   4. On Windows, optionally, uninstall WSL if only used for Nextstrain.

Next steps
==========

With Nextstrain installed, try :doc:`tutorials/running-a-workflow` next.
