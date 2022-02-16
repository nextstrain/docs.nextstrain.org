# Add your dataset to the collection of SARS-CoV-2 datasets

The nextstrain team maintains [nextstrain.org/sars-cov-2](https://nextstrain.org/sars-cov-2) to provide a resource for easy access to a variety of public analyses and interpretations by the Nextstrain team and the scientific community.

> During the pandemic we are focused on the SARS-CoV-2 page, but may generalize our approach in the future to provide similar resources for other pathogens.


To add a dataset to the SARS-CoV-2 datasets list on [nextstrain.org/sars-cov-2](https://nextstrain.org/sars-cov-2), create a pull request to the [nextstrain.org repository](https://github.com/nextstrain/nextstrain.org) on github using the following guide.
If this guide doesn't answer your questions or you aren't familiar with git, [open an issue in that same repository](https://github.com/nextstrain/nextstrain.org/issues/new/choose) letting us know about the dataset you would like to add, and we can help, or ask any question on [discussion.nextstrain.org](https://discussion.nextstrain.org/).

[Here is an example pull request](https://github.com/nextstrain/nextstrain.org/pull/246) for reference.

In the example above, a dataset is being added for Washington State, USA.
This is a dataset maintained by the Bedford Lab, focused on sequences from that area.
All information about this dataset is represented in the [YAML format](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) file in the nextstrain.org repository - [static-site/content/SARS-CoV-2-Datasets.yaml](https://github.com/nextstrain/nextstrain.org/blob/master/static-site/content/SARS-CoV-2-Datasets.yaml) - that contains the list of SARS-CoV-2 datasets.

In this case, this looks like the following:

```yaml
  - url: null
    name: Washington
    geo: washington
    parentGeo: usa
    org: null

  - url: https://nextstrain.org/groups/blab/ncov/wa/4m
    name: Washington
    geo: washington
    region: North America
    level: division
    coords:
      - -120.644869
      - 46.988611
    org:
      name: Bedford Lab
      url: https://bedford.io/
```

### Formatting

Spaces are used for indenting lines.
The YAML file contains one list of all entries.
The beginning section of the list contains hierarchy entries, while the latter section contains the dataset entries.

### Hierarchy entries

This YAML file defines a hierarchy of datasets according to their geographic specificity, which determines how datasets appear in dropdown menus.
Hierarchy entries in the list are just there to define this hierarchy with a `geo` field and a `parentGeo` field, like this one:
```
  - url: null
    name: Washington
    geo: washington
    parentGeo: usa
    org: null
```
Since Washington is in the USA, its `parentGeo` is `usa`.
At the [top of the hierarchy](https://github.com/nextstrain/nextstrain.org/blob/master/static-site/content/SARS-CoV-2-Datasets.yaml#L4) are hierarchy entries with the `parentGeo` value of `null`.
We add this entry since there already existed one for `usa`, but not for `washington` which is the `geo` level of the dataset entry we are adding.
The `url` and `org` fields are `null` since those only apply for dataset entries, but you no longer need to add these two extra fields as `null` anymore and can just leave them out like this:
```yaml
  - name: Washington
    geo: washington
    parentGeo: usa
```
If such an entry already existed for `washington`, we would only need to add the other type of entry - a dataset entry.

### Dataset entries

A dataset entry represents an actual dataset, and doesn't need the `parentGeo` field since it will get filed under the geographic region that matches its `geo` field:
```yaml
  - url: https://nextstrain.org/groups/blab/ncov/wa/4m
    name: Washington
    geo: washington
    region: North America
    level: division
    coords:
      - -120.644869
      - 46.988611
    org:
      name: Bedford Lab
      url: https://bedford.io/
```
Here is what each of these fields mean:

| Field | Example value | Description | Formatting |
|---|---|---|---|
|`url`| `https://nextstrain.org/groups/blab/ncov/wa/4m` | Link to the dataset | Valid unique url |
|`name` | `Washington` | A name for the dataset to be displayed on nextstrain.org  | Any informative string |
|`geo`|`washington`|Name of the geographic level|Lower case string consistent with `geo` hierarchy|
|`region`|N/A not used anymore.|||
|`level`|`region`, `country`, `division`, or `location` |Geographic specificity; see [here](https://docs.nextstrain.org/en/latest/tutorials/SARS-CoV-2/steps/data-prep.html#appendix-in-depth-guide-to-the-standard-nextstrain-metadata-fields) for more details. ||
|`coords`|`-120.644869`, `46.988611`|Longitutde and latitude in that order|Longitude: number between -180 (West) and 180 (East); Latitude: number between -85 (South) and 85 (North) |
|`org.name`|`Bedford Lab`|Who maintains this dataset? | String |
|`org.url`|`https://bedford.io/` |Link to info about the maintainers|Valid url|

#### `coords`

If there was already a dataset for `geo: washington` (or any dataset with nearby `coords`), we would need to be sure to specify coordinates that are not identical to those of the existing `washington` dataset so that you can see both on the map.
This will look different for different areas, since in some cases adjusting a latitude by 1 degree may be too much, and in other cases not enough.
There is a script, [`scripts/check-sars-cov-2-datasets-yaml.js`](https://github.com/nextstrain/nextstrain.org/blob/master/scripts/check-sars-cov-2-datasets-yaml.js), in the nextstrain.org repository which will tell you if two datasets' coordinates are too close to one another to be distinguished on the map.
