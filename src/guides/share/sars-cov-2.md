# Add your dataset to the SARS-CoV-2 build catalogue

The nextstrain team maintains [nextstrain.org/sars-cov-2](https://nextstrain.org/sars-cov-2) to provide a resource for easy access to a variety of public analyses and interpretations by the Nextstrain team and the scientific community.

> During the pandemic we are focused on the SARS-CoV-2 page, but may generalize our approach in the future to provide similar resources for other pathogens.


To add a build to the SARS-CoV-2 builds catalogue on [nextstrain.org/sars-cov-2](https://nextstrain.org/sars-cov-2), create a pull request to the [nextstrain.org repository](https://github.com/nextstrain/nextstrain.org) on github using the following guide.
If this guide doesn't answer your questions or you aren't familiar with git, [open an issue in that same repository](https://github.com/nextstrain/nextstrain.org/issues/new/choose) letting us know about the build you would like to add, and we can help, or ask any question on [discussion.nextstrain.org](https://discussion.nextstrain.org/).

[Here is an example pull request](https://github.com/nextstrain/nextstrain.org/pull/246) for reference.

In the example above, a build is being added for Washington State, USA.
This is a build maintained by the Bedford Lab, focused on sequences from that area.
All information about this build is represented in the [YAML format](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html) file in the nextstrain.org repository - [static-site/content/allSARS-CoV-2Builds.yaml](https://github.com/nextstrain/nextstrain.org/blob/master/static-site/content/allSARS-CoV-2Builds.yaml) - that contains the catalogue of SARS-CoV-2 builds.

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

## Formatting

Spaces are used for indenting lines.
The YAML file contains one list of all entries.
The beginning section of the list contains hierarchy entries, while the latter section contains the build entries.

### Hierarchy entries

This YAML file defines a hierarchy of builds according to their geographic specificity, which determines how builds appear in dropdown menus.
Hierarchy entries in the list are just there to define this hierarchy with a `geo` field and a `parentGeo` field, like this one:
```
  - url: null
    name: Washington
    geo: washington
    parentGeo: usa
    org: null
```
Since Washington is in the USA, its `parentGeo` is `usa`.
At the [top of the hierarchy](https://github.com/nextstrain/nextstrain.org/blob/master/static-site/content/allSARS-CoV-2Builds.yaml#L4) are hierarchy entries with the `parentGeo` value of `null`.
We add this entry since there already existed one for `usa`, but not for `washington` which is the `geo` level of the build entry we are adding.
The `url` and `org` fields are `null` since those only apply for build entries, but you no longer need to add these two extra fields as `null` anymore and can just leave them out like this:
```yaml
  - name: Washington
    geo: washington
    parentGeo: usa
```
If such an entry already existed for `washington`, we would only need to add the other type of entry - a build entry.

### Build entries

A build entry represents an actual build, and doesn't need the `parentGeo` field since it will get filed under the geographic region that matches its `geo` field:
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
|`url`| `https://nextstrain.org/groups/blab/ncov/wa/4m` | Link to the build | Valid unique url |
|`name` | `Washington` | A name for the build to be displayed on nextstrain.org  | Any informative string |
|`geo`|`washington`|Name of the geographic level|Lower case string consistent with `geo` hierarchy|
|`region`|N/A not used anymore.|||
|`level`|`region`, `country`, `division`, or `location` |Geographic specificity; see [here](https://docs.nextstrain.org/en/latest/tutorials/SARS-CoV-2/steps/data-prep.html#appendix-in-depth-guide-to-the-standard-nextstrain-metadata-fields) for more details. ||
|`coords`|`-120.644869`, `46.988611`|Longitutde and latitude in that order|Longitude: number between -180 (West) and 180 (East); Latitude: number between -85 (South) and 85 (North) |
|`org.name`|`Bedford Lab`|Who maintains this build? | String |
|`org.url`|`https://bedford.io/` |Link to info about the maintainers|Valid url|

#### `coords`

If there was already a build for `geo: washington` (or any build with nearby `coords`), we would need to be sure to specify coordinates that are not identical to those of the existing `washington` build so that you can see both on the map.
This will look different for different areas, since in some cases adjusting a latitude by 1 degree may be too much, and in other cases not enough.
There is a script, [`scripts/check-build-catalogue-yaml.js`](https://github.com/nextstrain/nextstrain.org/blob/master/scripts/check-build-catalogue-yaml.js), in the nextstrain.org repository which will tell you if two builds' coordinates are too close to one another to be distinguished on the map.

## Technical details

For SARS-CoV-2, [`scripts/collect-pathogen-resources.js`](https://github.com/nextstrain/nextstrain.org/blob/master/scripts/collect-pathogen-resources.js) is run like this:
```
scripts/collect-pathogen-resources.js --pathogen sars-cov-2
```
and reads in `static-site/content/allSARS-CoV-2Builds.yaml` and produces an augmented version of that YAML file called `allSARS-CoV-2Builds.augmented.yaml` with metadata from each build entry's corresponding dataset.
That augmented yaml file is stored in an s3 bucket and fetched by nextstrain.org to populate the front-end displays of the pathogen build catalogue (e.g. map of builds).

This process happens every weekday using [this Github Action](https://github.com/nextstrain/nextstrain.org/blob/master/.github/workflows/update-search.yml) in order to keep [nextstrain.org/sars-cov-2](https://nextstrain.org/sars-cov-2) up to date with all the datasets in the build catalogue.
This means that even once your PR is merged into the main branch of the nextstrain.org repository and your build has been added to the manually curated build catalogue, it may take a day or two before that is reflected on nextstrain.org.

### Testing
Once you have added your builds to the YAML file, if you want to see those changes immediately and you don't have access to the s3 bucket being used, you can make the following local changes to [`static-site/src/components/sars-cov-2/builds.jsx`](https://github.com/nextstrain/nextstrain.org/blob/master/static-site/src/components/sars-cov-2/builds.jsx):
```diff
+ import allSARSCoV2Builds from "../../../content/allSARS-CoV-2Builds.yaml";
  ...
  async componentDidMount() {
    try {
-     const catalogueBuilds = await fetchAndParseBuildCatalogueYaml(this.state.buildsUrl);
+     const catalogueBuilds = allSARSCoV2Builds;
      this.setState({catalogueBuilds, dataLoaded: true});
    } catch (err) {
      console.error("Error fetching / parsing data.", err.message);
      this.setState({errorFetchingData: true});
    }
  }
```

and run `cd nextstrain.org/static-site && npm run dev`.

This should work both with the manually curated version of the build catalogue yaml as well as an augmented version (e.g. `allSARS-CoV-2Builds.augmented.yaml` if you have run `scripts/collect-pathogen-resources.js --pathogen sars-cov-2` locally).

### Adding more metadata to the augmented YAML and accessing it on nextstrain.org

At the time of writing this doc, the augmented YAML with dataset metadata is a brand new feature and only the dataset's `meta.updated` property is attached as metadata to a build entry in the catalogue.
In order to extend this to attach other auspice dataset metadata to each build, the following steps are necessary:

1. Add the desired auspice dataset fieldnames to the [`getDatasetMetaProperties(dataset)`](https://github.com/nextstrain/nextstrain.org/pull/266/files#diff-60e76e88a4190ff6fcbe051a0db3f4289f7eb71dfa79f8f2f10d7e96b1fc6162R268) function in `scripts/collect-pathogen-resources.js`.
2. Run `scripts/collect-pathogen-resources.js` and make sure those properties are attached to the build entries as expected.
3. Access and display the property of the build in the desired react component on the front-end, [like this](https://github.com/nextstrain/nextstrain.org/pull/266/files#diff-0f173667f13492ac340f86da7913e9ca9b1ba4dd31e96264c5b7f99f2d0eb4baR225).
