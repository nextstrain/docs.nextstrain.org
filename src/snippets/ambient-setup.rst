1. Create a new Conda environment and install all the necessary software:

   .. code-block:: bash

      conda create -n <your-environment-name> \
            --override-channels --strict-channel-priority \
            -c conda-forge -c bioconda --yes \
            augur auspice nextclade \
            snakemake git epiweeks pangolin pangolearn \
            ncbi-datasets-cli csvtk seqkit tsv-utils

2. Activate the runtime:

   .. code-black:: bash

      conda activate <your-environment-name>

3. Set the runtime:

   .. code-block:: none

      nextstrain setup --set-default ambient
