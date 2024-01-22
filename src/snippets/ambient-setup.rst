1. Activate a Conda environment that you wish to use:

   .. code-block:: bash

      conda activate <your-environment-name>

2. Install all the necessary software:

   .. code-block:: bash

      conda install --override-channels --strict-channel-priority \
            -c conda-forge -c bioconda --yes \
            augur auspice nextclade \
            snakemake git epiweeks pangolin pangolearn \
            ncbi-datasets-cli

3. Set the runtime:

   .. code-block:: none

      nextstrain setup --set-default ambient
