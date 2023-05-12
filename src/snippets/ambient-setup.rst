1. Activate a Conda environment that you wish to use:

   .. code-block:: bash

      conda activate <your-environment-name>

2. Install all the necessary software:

   .. note::

      We recommend `Mamba <https://mamba.readthedocs.io>`_ as a drop-in replacement for ``conda`` to have faster installation times.

   .. code-block:: bash

      conda install --override-channels --strict-channel-priority \
            -c conda-forge -c bioconda --yes \
            augur auspice nextalign nextclade \
            snakemake git epiweeks pangolin pangolearn

3. Set the runtime:

   .. code-block:: none

      nextstrain setup --set-default ambient
