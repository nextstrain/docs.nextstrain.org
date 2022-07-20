.. code-block:: bash

    # Create and activate a "nextstrain" environment
    mamba create -n nextstrain
    conda activate nextstrain

    # Configure software channels; order is important!
    conda config --env --add channels defaults
    conda config --env --add channels bioconda
    conda config --env --add channels conda-forge
    conda config --env --set channel_priority strict
