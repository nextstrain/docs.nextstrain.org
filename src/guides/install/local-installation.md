# Local Installation


The following instructions describe how to install `augur` (bioinformatics tooling) and `auspice` (our visualization app) **together, in the same Conda environment**, on macOS or an Ubuntu-style Linux distribution.

> Before digging in, it's worth reading about [the different installation methods](./index) which will install the components behind Nextstrain and allow you to run and visualize analyses on your computer.

If you would prefer to install each component individually, please see the respective installation guides using the links in the sidebar.
If you are using Windows, we have instructions for [installing a Linux subsystem](./windows-help) to get Nextstrain running.
If you have any issues with installing Augur/Auspice using any of these methods, please [email us](mailto:hello@nextstrain.org) or submit a GitHub issue to [Augur](https://github.com/nextstrain/augur/issues) or [Auspice](https://github.com/nextstrain/auspice/issues).


---
## Install Augur & Auspice with Conda

[Download and install the latest version of Miniconda with Python 3](https://conda.io/miniconda.html) which will make the `conda` command available to you.
If you already have Miniconda installed with Python 2, download the latest Python 3 version and [follow conda's installation instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).
If you already have an older Miniconda version installed with Python 3, you may need to update your installation prior to installing Nextstrain's tools with:

```sh
conda activate base
conda update conda
```

We're going to create a new environment called "nextstrain", which automatically installs `Augur` and dependencies.
We'll then install `Auspice` into this environment as well, and optionally set up the `Nextstrain` command.


```sh
curl http://data.nextstrain.org/nextstrain.yml --compressed -o nextstrain.yml
conda env create -f nextstrain.yml
conda activate nextstrain
npm install --global auspice

# Optionally, if you want to use the nextstrain command
nextstrain check-setup --set-default
```

and we're all done 🙌.
The beauty of this is that whenever you want to use `augur` or `auspice` you can jump into the `nextstrain` conda environment and you're good to go!

```sh
conda activate nextstrain

# Test things are installed / run analyses
augur -h
auspice -h
nextstrain -h

# When you're done, leave the environment
conda deactivate
```


## Updating

> The following commands presume you have installed the software via the method described above.

Firstly, ensure that `conda` itself is up-to-date!
```sh
conda activate base
conda update conda
conda activate nextstrain
```

Then we can update each individual piece, as necessary:

```sh
python3 -m pip install --upgrade nextstrain-cli
conda install --update-deps -c conda-forge -c bioconda augur # will also update mafft etc
npm update --global auspice
```
