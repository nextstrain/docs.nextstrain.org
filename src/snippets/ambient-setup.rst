1. Create a new Conda environment and install Python 3.10.13:

   .. code-block:: bash

      conda create -n <your-environment-name>
      conda activate <your-environment-name>
      conda install --override-channels --strict-channel-priority \
            -c conda-forge --yes python=3.10.13

2. Install all the necessary software:

   .. code-block:: bash

      conda install --override-channels --strict-channel-priority \
            -c conda-forge -c bioconda --yes \
            augur auspice nextclade \
            snakemake git epiweeks pangolin pangolearn \
            ncbi-datasets-cli csvtk seqkit tsv-utils

3. Set the runtime:

   .. code-block:: none

      nextstrain setup --set-default ambient
