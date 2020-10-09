# docs.nextstrain.org

A prototype umbrella documentation project for Nextstrain, hosted at [docs.nextstrain.org](https://docs.nextstrain.org), using:

- [Read The Docs](https://readthedocs.org)
- [Sphinx](http://sphinx-doc.org)
- [Markdown](https://markdownguide.org) and [reStructuredText](https://docutils.sourceforge.io/rst.html) ([quick ref](https://docutils.sourceforge.io/docs/user/rst/quickref.html), [quicker ref](https://simonwillison.net/2018/Aug/25/restructuredtext/))
- [Subprojects](https://docs.readthedocs.io/en/stable/subprojects.html) for Augur and the CLI (plus maybe Auspice and other component/build-specific documentation in the future)
- Our custom [Sphinx theme](https://github.com/nextstrain/sphinx-theme) to provide consistent, branded styling.

## What technologies are used to build it and what part does each play? include a glossary / link to key terms for each of these
TODO

## Domain management
To manage the hosting settings of docs.nextstrain.org and monitor automated builds triggered by pushes to this repository, go to https://readthedocs.org/projects/nextstrain/.
You'll need to create an account and be granted permissions to view and edit admin settings for the project by someone on the Nextstrain team.

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

### Build configuration

Read the docs is configured via `readthedocs.yml`; [more about Read the docs configuration](https://docs.readthedocs.io/en/stable/config-file/v2.html)

Sphinx is configured via `src/conf.py`; [more about Sphinx configuration](https://www.sphinx-doc.org/en/master/usage/configuration.html)

## Migration of Nextstrain docs to this repository
We have agreed on some major headings and subheadings [1] for an all-Nextstrain documentation project in this repo.
We are using the migrate branch to move individual documents over to this Read the Docs project, under those headings.
We are tracking progress of migration-related tasks in a github project [2].
[1] https://docs.google.com/document/d/1hq6hjukg3Pw8m12Y0IaephQYJCFvpFrChl0K0B_4UrQ/edit#heading=h.t0j8btmy5ggi
[2] https://github.com/nextstrain/docs.nextstrain.org/projects/1

## TODO Philosophy / documentation system

## Implementation
What is our implementation using these technologies? Maybe a diagram if necessary with respect to submodules, subprojects
### File Hierarchy, Formats
The hierarchy of the table of contents as seen in the sidebar can be thought of as a tree of documents.
The root is `src/index.rst` a restructured text (more on this below TODO insert link to rst section) file which dictates what the top-level headings in the sidebar will be.
It contains a `.. toctree::` "directive" or statement, followed by some configuration and then a list of file paths:
```
======================================
Welcome to Nextstrain's documentation!
======================================

Nextstrain is an open-source project to harness the scientific and public health potential of pathogen genome data.
We provide a continually-updated view of publicly available data with powerful analyses and visualizations showing pathogen evolution and epidemic spread.
Our goal is to aid epidemiological understanding and improve outbreak response.
If you have any questions, or simply want to say hi, please give us a shout at hello@nextstrain.org.

.. warning::
   This site is currently only a stub, to show what's possible with Read The Docs for an umbrella documentation project.

   For the real documentation entry point, please go to `nextstrain.org/docs <https://nextstrain.org/docs>`__.

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :caption: Table of contents

   self
   learn/index
   tutorials/index
   guides/index
   reference/index
```
These file paths such as `learn/index` are what show up in the sidebar at the top level. 
In this case, each of the paths specified is another restructured text(.rst - but the file extension is omitted in the `toctree` listing) file, containing a similar statement, listing the files for that section.
However, you can also list paths to regular markdown documents (also without extension) which will just render a clickable entry in the sidebar to navigate to that document, and it will not be an expandable section.
If any file contains a valid one of these `.. toctree::` statements, it will be rendered as an expandable heading in the sidebar, with the `toctree` entries rendered under that heading.

More on this in the [Sphinx Documentation](https://www.sphinx-doc.org/en/1.5/markup/toctree.html).

#### Restructured text
TODO some helpful links on rst formatting

### Subprojects
TODO general intro to subprojects (dont duplicate things that I can just link here from RTD docs!!)

TODO make this info about how we organize things into something useful
Part of the philosophy was that the sub-projects are repo-specific and those documents which we've made accessible in the main project (but still live in their respective repositories, i.e. those docs which we include from the submodules) seemed non-repo-specific, so we wanted to make them more accessible without having to know that one needs to find them in a particular repo's subproject, since the subprojects are somewhat "siloed" from the main project as @jameshadfield raised in some initial discussions on this.
Meanwhile, we've left "reference guide" material in the subprojects to be linked to from the main project, since reference guides do feel repo-specific.

You're right on as far as I'm concerned: at least one challenge that presented there was if we wanted to include things like the augur api auto-generated docs there, it seemed like the options (assuming we wanted to maintain the versioning of those docs from the augur repo's git tags) were:
via submodules - this doesn't achieve the goal of maintaining the version but does put it into the same toctree
via subprojects - we went with this since it preserves versioning of those docs according to augur versioning; even though it may be siloed, at least it is content that you might expect in that silo
but I definitely am no RTD or RsT expert so maybe we missed how to get the best of both worlds.

### Submodules
In many cases this will involve moving the document so that it is stored in this repository and adding the necessary Read the Docs directive to the document to surface the document in the table of contents / in the sidebar.
In some other cases, where it makes more sense to store the document in a different repository, we will need to include the document directly from it's home repository; the current plan for this is using submodules - see the following section for details on how to do this.


### How we use submodules to source documents from other repositories

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

## Contributing
TODO Somewhat robust instructions on how to contribute docs work building from / referring to the implementation section above
### How-to tips
TODO List of tips / tricks for RsT, RTD, etc
