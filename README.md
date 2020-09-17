# docs.nextstrain.org

A prototype umbrella documentation project for Nextstrain, hosted at [docs.nextstrain.org](https://docs.nextstrain.org), using:

- [Read The Docs](https://readthedocs.org)
- [Sphinx](http://sphinx-doc.org)
- [Markdown](https://markdownguide.org) and [reStructuredText](https://docutils.sourceforge.io/rst.html) ([quick ref](https://docutils.sourceforge.io/docs/user/rst/quickref.html), [quicker ref](https://simonwillison.net/2018/Aug/25/restructuredtext/))
- [Subprojects](https://docs.readthedocs.io/en/stable/subprojects.html) for Augur and the CLI (plus maybe Auspice and other component/build-specific documentation in the future)
- Our custom [Sphinx theme](https://github.com/nextstrain/sphinx-theme) to provide consistent, branded styling.

## Building the docs

Build dependencies are managed with [Conda](https://conda.io).  Install them
into an isolated environment named `docs.nextstrain.org` with:

    conda env create

Enter the environment with:

    conda activate docs.nextstrain.org

You can now build the documentation with:

    make html

which invokes Sphinx to build static HTML pages in `build/html/`.  You can view
them by running:

    open build/html/index.html

Leave the environment with:

    conda deactivate

## Migrating docs content to this repository

We have agreed on some major headings and subheadings [1] for an all-Nextstrain documentation project in this repo.
The plan is to use the migrate branch to move individual documents over to this Read the Docs project, under those headings.
In many cases this will involve moving the document so that it is stored in this repository and adding the necessary Read the Docs directive to the document to surface the document in the table of contents / in the sidebar.
In some other cases, where it makes more sense to store the document in a different repository, we will need to include the document directly from it's home repository; the current plan for this is using submodules - see the following section for details on how to do this.

[1] https://docs.google.com/document/d/1hq6hjukg3Pw8m12Y0IaephQYJCFvpFrChl0K0B_4UrQ/edit#heading=h.t0j8btmy5ggi

### Using submodules to import documents from other repositories

1. Make sure you are on the latest `migrate` branch: `git clone https://github.com/nextstrain/docs.nextstrain.org.git && cd docs.nextstrain.org && git checkout migrate`
2. Fetch any existing submodules `submodule update --init --recursive`
3. Change to the `src` directory and add the submodule for the repository from which you would like to include document(s), e.g. `cd src && git submodule add https://github.com/nextstrain/augur.git`
4. Add the submodule to `readthedocs.yml`, e.g.:
```
 ---
 version: 2
 conda:
   environment: environment.yml
 submodules:
   include:
      - src/ncov
+     - src/augur
```
5. Now you may include any document from your submodule directory, `src/augur` by including the relative path to the document in a table of contents specification in a restructured text file like `src/guides/share/index.rst`:
```
 ======================================
 Visualizing and Sharing Analyses
 ======================================
 
 How-to guides for visualizing and sharing Nextstrain analyses.
 
 .. toctree::
    :maxdepth: 2
    :titlesonly:
    :caption: Table of contents
 
+   ../../augur/docs/faq/community_hosting
```
6. After building the docs (see above section), the `/guides/share/` section should include the document from the submodule in its table of contents: ![](images/submodule_eg.png)
