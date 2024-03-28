========
Glossary
========

.. glossary::

   Augur

      A command-line application used for phylogenetic analysis. :doc:`Documentation<augur:index>`

   Auspice

      A web application used for phylogenetic visualization and analysis. :doc:`Documentation<auspice:index>`

   pathogen repository

      A version-controlled folder containing all files necessary to run a pathogen's :term:`workflows<workflow>`.

   workflow

      A reproducible process comprised of one or more :term:`builds<build>` producing :term:`datasets<dataset>`.
      Implementation varies per workflow, but generally they are run by workflow managers such as Snakemake.

      A Nextstrain :term:`pathogen repository` typically consists of these different workflows

      1. :term:`phylogenetic workflow`
      2. :term:`ingest workflow`
      3. :term:`Nextclade workflow`

      Our :term:`core workflows<core workflow>` can be divided into two types:

      1. Single-build workflow (e.g. Zika workflow): one build producing one dataset.
      2. Multi-build workflow (e.g. SARS-CoV-2 workflow): multiple builds producing multiple datasets.

      .. note::

         The individual builds in a multi-build workflow are also "workflows" in the definition of workflow managers like Snakemake.

   phylogenetic workflow
      also *Nextstrain workflow*

      A :term:`workflow` consisting of :term:`build(s)<build>` that execute bioinformatic analyses with :term:`Augur` to generate
      :term:`phylogenetic dataset(s)<phylogenetic dataset>` for visualization with :term:`Auspice`.

      The phylogenetic workflow is often considered the primary workflow in a pathogen repository
      (e.g. "the Zika workflow" typically means "the phylogenetic workflow in the Zika pathogen repository").

   ingest workflow

      A :term:`workflow` consisting of :term:`build(s)<build>` that curate public metadata and sequences to generate
      :term:`ingest dataset(s)<ingest dataset>` that are typically used as input files for
      :term:`phylogenetic workflows<phylogenetic workflow>` and :term:`Nextclade workflows<Nextclade workflow>`.

   Nextclade workflow

      A :term:`workflow` consisting of :term:`build(s)<build>` that generate :doc:`reference tree(s)<nextclade:user/input-files/04-reference-tree>` to be packaged with other
      dataset files to create :term:`Nextclade dataset(s)<Nextclade dataset>`.

   core workflow

      A :term:`workflow` maintained by the Nextstrain team.

   build
      also *Nextstrain build*, *phylogenetic build*, *ingest build*, *Nextclade build*

      *(noun)* A sequence of commands, parameters and input files which work together to reproducibly generate a :term:`dataset`.

   build (verb)

      A general term for running a :term:`workflow` (e.g. ``nextstrain build``).

   build step

      A modular instruction of a :term:`build` which can be run standalone (e.g. ``augur filter``), often with clear input and output files.

   dataset

      A collection of output files produced by a :term:`build`.
      A Nextstrain :term:`pathogen repository` typically produces multiple types of datasets

      1. :term:`phylogenetic dataset`
      2. :term:`ingest dataset`
      3. :term:`Nextclade dataset`

   phylogenetic dataset
      also *Auspice JSONs*

      A :term:`dataset` consisting of :term:`JSONs` produced by a :term:`build` of a :term:`phylogenetic workflow`.
      It is also the shared file prefix of the JSONs.
      For example ``flu/seasonal/h3n2/ha/2y`` identifies a dataset which corresponds to the files:

      - ``flu_seasonal_h3n2_ha_2y_meta.json``
      - ``flu_seasonal_h3n2_ha_2y_tree.json``
      - ``flu_seasonal_h3n2_ha_2y_tip-frequencies.json``

      Some phylogenetic workflows produce a single, synonymous dataset, like Zika. Others, like seasonal flu, produce many datasets.
      The phylogenetic dataset is often considered the primary dataset in a pathogen repository
      (e.g. "the Zika dataset" typically means "the phylogenetic dataset from the Zika pathogen repository").

   ingest dataset

      A :term:`dataset` consisting of curated files produced by a :term:`build` of an :term:`ingest workflow`.
      Typically consists of the files:

      * metadata.tsv
      * sequences.fasta

      If the ingest workflow includes Nextclade :term:`build steps<build step>`, then the dataset will typically include
      :doc:`Nextclade output files<nextclade:user/output-files/index>` as well.

   Nextclade dataset

      A :term:`dataset` consisting of files required for a :doc:`Nextclade<nextclade:index>` analysis, usually produced
      by a :term:`build` of a :term:`Nextclade workflow`.
      See :doc:`documentation<nextclade:user/datasets>` for more details

   narrative

      A method of data-driven storytelling with interactive views of :term:`phylogenetic datasets<phylogenetic dataset>` displayed alongside multiple pages (or slides) of text and images.
      Saved as a Markdown file with extended syntax to support additional displays.

      Viewable on nextstrain.org or with :term:`Auspice` via the :doc:`cli:commands/view` or :doc:`auspice view <auspice:introduction/how-to-run>` commands.

      See also :doc:`/guides/communicate/narratives-intro` and :doc:`/tutorials/narratives-how-to-write`.

   JSONs
      Special ``.json`` files produced by :term:`Augur` and visualized by :term:`Auspice`. These files make up a :term:`phylogenetic dataset`.
      See :doc:`data formats<data-formats>`.

   Nextstrain CLI

      The Nextstrain command-line interface (**Nextstrain CLI**) provides a consistent way to run and visualize :term:`pathogen builds<Build>` and access Nextstrain components like :term:`Augur` and :term:`Auspice` across :term:`runtimes<runtime>` such as Docker, Conda, and AWS Batch.

      :doc:`Documentation <cli:index>`

   runtime
      also *Nextstrain runtime*

      When installing and using the :term:`Nextstrain CLI`, there are different configuration options, or **runtimes**, depending on the operating system.

      1. Docker runtime
      2. Conda runtime
      3. Ambient runtime (:ref:`formerly "native" <what-happened-to-the-native-runtime>`)
      4. AWS Batch runtime (only for ``nextstrain build``)
