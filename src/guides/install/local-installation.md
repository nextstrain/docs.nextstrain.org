# Local Installation


The following instructions describe how to install `augur` (bioinformatics tooling) and `auspice` (our visualization app) on macOS or an Ubuntu-style Linux distribution using Conda.

> Before digging in, it's worth reading about [the different installation methods](./index) which will install the components behind Nextstrain and allow you to run and visualize analyses on your computer.

If you would prefer to install each component individually, please see the respecive installation guides using the links in the sidebar. 
If you are using Windows, we have instructions for [installing a Linux subsystem](./windows-help) to get Nextstrain running.
If you have any issues with installing Augur/Auspice using any of these methods, please [email us](mailto:hello@nextstrain.org) or submit a GitHub issue to [Augur](https://github.com/nextstrain/augur/issues) or [Auspice](https://github.com/nextstrain/auspice/issues).


---
## Install Augur & Auspice with Conda

[Download and install the latest version of Miniconda](https://conda.io/miniconda.html) which will make the `conda` command available to you.
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


## Updating `augur`, `auspice`, and `nextstrain`:

```sh
conda activate nextstrain
pip install --upgrade nextstrain-augur nextstrain-cli
npm update --global auspice
```
