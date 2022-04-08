# Share via Community on GitHub

One of [the ways](./index) we allow researchers to share their analyses through Nextstrain is via [GitHub](https://github.com).
This allows dataset JSONs and/or narrative markdown files to be stored in your own GitHub repos and accessed through [nextstrain.org/community](https://nextstrain.org/community) URLs.
This gives you complete control, ownership, and discretion over your data.
All that is required for this funcitonality is for files to conform to a specific naming scheme (see below).
There is no need to get in touch with the Nextstrain team to allow access to the dataset, but if you would like your dataset featured on the [front page](https://nextstrain.org/community) or to be listed along with all available [SARS-CoV-2 builds](https://nextstrain.org/sars-cov-2/) then please [let us know!](mailto:hello@nextstrain.org)

P.S. For help with running your analysis, [see the bioinformatics introduction](https://docs.nextstrain.org/projects/augur/en/stable/index.html).

## Technical details

Given a github organisation `<ORG>` and repository `<REPO>`, dataset files should be stored in a folder named `auspice`.
The filename must have the format `<REPO>[_<NAME1>[_<NAME2>[...]]].json`, where underscore-separated dataset-specific names (e.g. `<NAME1>`) are optional.
Such datasets will be available at `nextstrain.org/community/<ORG>/<REPO>[/<NAME1>/<NAME2>/...]`. Note that dataset names are `/`-separated in the URL.
See the table below for examples.

**Git Branches** In the above description, files are assumed to reside on the `master` branch.
It is possible to access files on a different branch, `<BRANCH>` by specifying the branch in the URL via `nextstrain.org/community/<ORG>/<REPO>@<BRANCH>[/<NAME1>/...]`.
Note that if the default branch on your repo is `main` then you must specify this in the URL, e.g. `nextstrain.org/community/<ORG>/<REPO>@main`.
See the table below for examples.

**Listing of all datasets and narratives**
If a dataset file exists at `auspice/<REPO>.json` (i.e. there are no dataset specific names in the filename) then visiting `nextstrain.org/community/<ORG>/<REPO>` will automatically load that dataset.
If such a file does not exist (i.e. all the datasets have at least one `<NAME>` in their filenames) then visiting that URL will list the available datasets and narratives.

**Narratives**
The above naming scheme is the same for narratives, with a few small changes.
Files should be located in the `narratives` folder (not `auspice`), they should have a `.md` suffix (not `.json`) and are accessed through URLS `nextstrain.org/community/narratives/<ORG>/<REPO>[/<NAME1>/...]`.
See the table below for examples.
See the table below for an example.

**v1 (deprecated) datasets** work the same way, except that there are two JSONs required, `auspice/<REPO>[_<NAME1>...]_tree.json` and `auspice/<REPO>[_<NAME1>...]_meta.json`.
Note that if there is a unified dataset also available (`auspice/<REPO>[_<NAME1>...].json`) then this will be preferentially used.
See "zika-colombia" in the table below as an example.

## Examples

**Datasets**

(GitHub) Org      | Repository   | branch    | File(s) in repository    | Nextstrain URL
-------- | ------ | --------- | --------------- | ------------
`<ORG>`   | `<REPO>` | master    | `auspice/<REPO>.json` | `nexstrain.org/community/<ORG>/<REPO>`
`<ORG>`   | `<REPO>` | `<BRANCH>`    | `auspice/<REPO>.json` | `nexstrain.org/community/<ORG>/<REPO>@<BRANCH>`
`<ORG>`   | `<REPO>` | `<BRANCH>`    | `auspice/<REPO>_<NAME1>_<NAME2>.json` | `nexstrain.org/community/<ORG>/<REPO>@<BRANCH>/NAME1/NAME2`
[blab](github.com/blab/) | [sars-like-cov](https://github.com/blab/sars-like-cov) | master | [auspice/sars-like-cov.json](https://github.com/blab/sars-like-cov/blob/master/auspice/sars-like-cov.json) | https://nextstrain.org/community/blab/sars-like-cov
[emmahodcroft](https://github.com/emmahodcroft) | [cov](https://github.com/emmahodcroft/cov) | master | N/A | https://nextstrain.org/community/emmahodcroft/cov (lists available datasets)
[emmahodcroft](https://github.com/emmahodcroft) | [cov](https://github.com/emmahodcroft/cov) | master | [auspice/cov_229E_spike.json](https://github.com/emmahodcroft/cov/blob/master/auspice/cov_229E_spike.json) | https://nextstrain.org/community/emmahodcroft/cov/229E/spike
[emmahodcroft](https://github.com/emmahodcroft) | [cov](https://github.com/emmahodcroft/cov) | master | [auspice/cov_OC43_spike.json](https://github.com/emmahodcroft/cov/blob/master/auspice/cov_OC43_spike.json) | https://nextstrain.org/community/emmahodcroft/cov/OC43/spike
[jameshadfield](github.com/jameshadfield/) | [scratch](https://github.com/jameshadfield/scratch) | [test-branch](https://github.com/jameshadfield/scratch/tree/test-branch) | [auspice/scratch_placentalia.json](https://github.com/jameshadfield/scratch/blob/test-branch/auspice/scratch_placentalia.json) | https://nextstrain.org/community/jameshadfield/scratch@test-branch/placentalia
[blab](github.com/blab/) | [zika-colombia](https://github.com/blab/zika-colombia) | master | [auspice/zika-colombia_meta.json](https://github.com/blab/zika-colombia/blob/master/auspice/zika-colombia_meta.json), <br> [auspice/zika-colombia_tree.json](https://github.com/blab/zika-colombia/blob/master/auspice/zika-colombia_tree.json) | https://nextstrain.org/community/blab/zika-colombia


**Narratives**

(GitHub) Org      | Repository   | branch    | File(s) in repository    | Nextstrain URL
-------- | ------ | --------- | --------------- | ------------
`<ORG>`   | `<REPO>` | master    | `narratives/<REPO>.json` | `nexstrain.org/community/<ORG>/<REPO>`
ESR-NZ | GenomicsNarrativeSARSCoV2 | [master](https://github.com/ESR-NZ/GenomicsNarrativeSARSCoV2/tree/master) | [narratives/GenomicsNarrativeSARSCoV2_2020-10-01.md](https://github.com/ESR-NZ/GenomicsNarrativeSARSCoV2/blob/master/narratives/GenomicsNarrativeSARSCoV2_2020-10-01.md) | https://nextstrain.org/community/narratives/ESR-NZ/GenomicsNarrativeSARSCoV2/2020-10-01
[blab](github.com/blab/) | [ebola-narrative-ms](https://github.com/blab/ebola-narrative-ms/) | master | [narratives/ebola-narrative-ms_2019-09-13-sit-rep-ENGLISH.md](https://github.com/blab/ebola-narrative-ms/blob/master/narratives/ebola-narrative-ms_2019-09-13-sit-rep-ENGLISH.md) | https://nextstrain.org/community/narratives/blab/ebola-narrative-ms/2019-09-13-sit-rep-ENGLISH

For more examples please see the [Nextstrain front page](https://nextstrain.org/community) and the listing of all [SARS-CoV-2 builds](https://nextstrain.org/sars-cov-2/).


