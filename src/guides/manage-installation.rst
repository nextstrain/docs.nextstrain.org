==================================
Managing a Nextstrain Installation
==================================

This page is for users who have already finished :doc:`/install`.

Steps vary by runtime option (Docker, Conda, ambient). To determine which Nextstrain runtime you are using, run:

.. code-block:: bash

   nextstrain version --verbose

and look for the name that has ``(default)`` next to it.


.. contents:: Table of Contents
   :local:


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


   .. group-tab:: Singularity (Apptainer)

      Update the Singularity runtime:

      .. code-block:: bash

         nextstrain update singularity

      If the output notes that an update of the Nextstrain CLI itself is available, run the suggested command (after optionally reviewing the release notes).


   .. group-tab:: Ambient (advanced)

      Update a custom Conda environment.

      .. code-block:: bash

         conda activate <your-environment-name>
         conda update --all
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


   .. group-tab:: Singularity (Apptainer)

      Running ``nextstrain check-setup singularity`` will report potential issues.
      Make sure there are no errors or warnings reported.

      You can forcibly setup the Singularity runtime again by running:

      .. code-block:: bash

         nextstrain setup --force singularity

      This should rarely be necessary, but may help if you find yourself with a broken runtime.


   .. group-tab:: Ambient (advanced)

      Running ``nextstrain check-setup ambient`` will report potential issues.
      Make sure there are no errors or warnings reported.

      If tools were installed into a custom Conda environment, ensure that it's activated with ``conda activate <your-environment-name>``.

      If Conda fails to install or update Nextstrain using the commands in the other sections above, it's possible that Conda itself is out-of-date or that Conda cannot figure out how to resolve the environment's dependencies.
      Starting from scratch often fixes problems with Conda environments.
      To start over with a new Nextstrain environment, delete your current environment.

      .. code-block:: bash

          conda env remove -n <your-environment-name>

      Then, repeat the Ambient runtime setup instructions above.

If you the above isn't sufficient and you need more help troubleshooting, please post to our `discussion forum <https://discussion.nextstrain.org/c/help-and-getting-started/6>`__ where members of the community and the Nextstrain team can help out.


Uninstall
=========

We do not have an automated uninstall process currently.
Instead, follow these manual steps:

   1. If the directory :file:`~/.nextstrain` exists, remove it.
   2. If using the Docker runtime, remove all ``nextstrain/…`` Docker images::

         docker image rm $(docker image ls -q "nextstrain/*")

      Optionally, uninstall Docker if only used for Nextstrain.
   3. If using the ambient runtime, remove the custom Conda environment::

         conda env remove -n <your-environment-name>

      Optionally, uninstall Conda if only used for Nextstrain.
   4. On Windows, optionally, uninstall WSL if only used for Nextstrain.
