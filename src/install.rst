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

Steps vary by runtime option (Docker, native) and operating system (macOS, Windows, WSL on Windows, Linux).
For help choosing, refer to our :doc:`/reference/faq`, such as:

  * :ref:`what-are-docker-conda-mamba-wsl-etc`
  * :ref:`choosing-a-runtime`
  * :ref:`when-to-use-wsl`

First, install a Nextstrain runtime.

.. tabs::

   .. group-tab:: Docker

      .. tabs::

         .. group-tab:: macOS

            .. warning::

               If using a newer Mac with an `Apple silicon chip <https://support.apple.com/en-us/HT211814>`_ (e.g. M1), the **native** runtime is recommended due to slowness with the Docker runtime. `We are considering ways to improve this <https://github.com/nextstrain/docker-base/issues/35>`_.

            1. `Install Docker Desktop using the official guide <https://docs.docker.com/desktop/install/mac-install/>`_.
            2. Install the Nextstrain CLI:

               .. code-block:: bash

                  curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/mac | bash

            3. Follow the installer's final instructions to setup your shell config.


         .. group-tab:: Windows

            1. `Install Windows Subsystem for Linux (WSL) 2 <https://docs.microsoft.com/en-us/windows/wsl/install>`_.

               .. note:: You may have to restart your machine when configuring WSL.

            2. `Install Docker Desktop <https://docs.docker.com/desktop/install/windows-install/>`_ with the `WSL 2 backend <https://docs.docker.com/desktop/windows/wsl/>`_.
            3. Open a PowerShell prompt (not a WSL prompt) as your own user (not as an administrator).
            4. Install the Nextstrain CLI.

               .. code-block:: powershell

                  Invoke-RestMethod https://nextstrain.org/cli/installer/windows | Invoke-Expression


         .. group-tab:: WSL on Windows

            1. `Install Windows Subsystem for Linux (WSL) 2`_.

               .. note:: You may have to restart your machine when configuring WSL.

            2. `Install Docker Desktop`_ with the `WSL 2 backend`_.

               .. note:: Make sure to follow through the last step of enabling **WSL Integration**.

            3. Open a WSL terminal by running **wsl** from the Start menu.
            4. Install the Nextstrain CLI:

               .. code-block:: bash

                  curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

            5. Follow the installer's final instructions to setup your shell config.

            .. include:: snippets/wsl-home-dir.rst


         .. group-tab:: Ubuntu Linux

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
            4. Install the Nextstrain CLI:

               .. code-block:: bash

                  curl -fsSL --proto '=https' https://nextstrain.org/cli/installer/linux | bash

            5. Follow the installer's final instructions to setup your shell config.


   .. group-tab:: Native

      .. tabs::

         .. group-tab:: macOS

            1. Install Miniconda:

               .. The installer link is taken from https://docs.conda.io/en/latest/miniconda.html.

               a. `Download the installer <https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg>`_.

                  .. note::

                        This is the Intel x86 64-bit installer, :ref:`which we recommend even for Mac computers with Apple silicon (e.g. M1) <why-intel-miniconda-installer-on-apple-silicon>`.

               b. Open the downloaded file and follow through installation prompts.

            2. Open a terminal window.
            3. Install Mamba on the ``base`` Conda environment:

               .. code-block:: bash

                  conda install -n base -c conda-forge mamba --yes
                  conda activate base

            4. Create a Conda environment named ``nextstrain``:

               .. include:: snippets/conda-create-bash.rst

            5. Install all the necessary software:

               .. include:: snippets/conda-install-full-bash.rst


         .. group-tab:: Windows

            .. note::

               Due to installation constraints, there is no way to use the native runtime on Windows directly. Follow steps for **WSL on Windows** if the native runtime is desired, or use the **Docker**-based steps instead.


         .. group-tab:: WSL on Windows

            1. `Install Windows Subsystem for Linux (WSL) 2`_.
            2. Open a WSL terminal by running **wsl** from the Start menu.
            3. Install Miniconda:

               .. code-block:: bash

                  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
                  bash Miniconda3-latest-Linux-x86_64.sh
                  # follow through installation prompts
                  rm Miniconda3-latest-Linux-x86_64.sh

            3. Install Mamba on the ``base`` Conda environment:

               .. code-block:: bash

                  conda install -n base -c conda-forge mamba --yes
                  conda activate base

            4. Create a Conda environment named ``nextstrain``:

               .. include:: snippets/conda-create-bash.rst

            5. Install all the necessary software:

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

            3. Create a Conda environment named ``nextstrain``:

               .. include:: snippets/conda-create-bash.rst

            4. Install all the necessary software:

               .. include:: snippets/conda-install-full-bash.rst

      .. admonition:: For native runtime installs
         :class: hint

         Whenever you open a new terminal window to work on a Nextstrain analysis, remember to activate the Conda environment with ``conda activate nextstrain``.



Then, confirm that the installation worked.

.. code-block:: bash

  nextstrain check-setup --set-default

The final output from the last command should look like this, where ``<runtime>`` is the runtime option (e.g. ``docker`` or ``native``) chosen in the first step:

.. code-block:: none

  Setting default environment to <runtime>.

Optionally, :doc:`configure AWS Batch <cli:aws-batch>` if you'd like to run ``nextstrain build`` on AWS.

Next, try :doc:`tutorials/running-a-workflow`.


Update an existing installation
================================

.. tabs::

   .. group-tab:: Docker

      Download the latest image with the Nextstrain CLI.

      .. code-block:: bash

         nextstrain update

      If the output notes that an update of the Nextstrain CLI itself is available, run the suggested command (after optionally reviewing the release notes).


   .. group-tab:: Native

      Update the ``nextstrain`` Conda environment.

      .. code-block:: bash

         mamba update -n base conda mamba
         conda activate nextstrain
         mamba update --all


Troubleshoot a broken installation
==================================

.. tabs::

   .. group-tab:: Docker

      The Docker runtime requires that the Docker service is running on your computer behind the scenes.
      If you see a message like::

         Cannot connect to the Docker daemon at […]. Is the docker daemon running?

      Then it is likely that the Docker service is not running.
      On macOS and Windows, try quitting Docker Desktop (if it's open) and restarting it.
      On Linux, try running ``sudo systemctl restart docker``.

      Running ``nextstrain check-setup`` will also report potential issues.
      Make sure there are no errors or warnings reported for the Docker runtime.


   .. group-tab:: Native

      If Conda fails to install or update Nextstrain using the commands above, it's possible that Conda itself is out-of-date or that Conda cannot figure out how to resolve the environment's dependencies.
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

.. tabs::

   .. group-tab:: Docker

      1. If the directory :file:`~/.nextstrain` exists, remove it.
      2. Remove all ``nextstrain/…`` Docker images::

            docker image rm $(docker image ls -q "nextstrain/*")

      3. Optionally, uninstall Docker if only used for Nextstrain.
      4. On Windows, optionally, uninstall WSL if only used for Nextstrain.

   .. group-tab:: Native

      1. If the directory :file:`~/.nextstrain` exists, remove it.
      2. Remove the ``nextstrain`` Conda environment::

            conda env remove -n nextstrain

      3. Optionally, uninstall Conda if only used for Nextstrain.
      4. On Windows, optionally, uninstall WSL if only used for Nextstrain.

Next steps
==========

With Nextstrain installed, try :doc:`tutorials/running-a-workflow` next.
