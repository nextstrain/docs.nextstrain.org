.. code-block:: bash

   mamba create -n nextstrain \
     -c conda-forge -c bioconda -c defaults --strict-channel-priority --yes \
     nextstrain-cli augur auspice nextalign nextclade snakemake git epiweeks pangolin pangolearn
