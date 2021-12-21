========
Glossary
========

.. glossary::

   Augur

      A command-line application used for phylogenetic analysis. :doc:`Documentation<augur:index>`

   Auspice

      A web application used for phylogenetic visualization and analysis. :doc:`Documentation<auspice:index>`

   workflow
      also *pathogen workflow*

      A sequential process producing one or more :term:`datasets<dataset>`, which can be visualized by :term:`Auspice`.

      Our core workflows can be divided into two types:

      1. Single-build workflow (e.g. Zika workflow): one build, one dataset.
      2. Multi-build workflow (e.g. SARS-CoV-2 workflow): multiple builds, multiple datasets.

      .. note::

         The individual builds in a multi-build workflow are also "workflows" in the definition of workflow managers like Snakemake.

   build

      *(noun)* A set of commands, parameters and input files which work together to reproducibly execute bioinformatic analyses and generate a :term:`dataset` for visualization with :term:`Auspice`.

   build (verb)

      A general term for running a :term:`workflow` (e.g. ``nextstrain build``).

   build step

      A modular instruction of a :term:`build` which can be run standalone (e.g. ``augur filter``), often with clear input and output files.

   build script

      In :term:`single-build workflows<workflow>`, a **build script** (e.g. ``Snakefile``) is used to chain together :term:`build steps<build step>` and runnable with a single command. The script is contained in a folder alongside other necessary files.

      In complex workflows, like SARS-CoV-2, there is no singular build script.

   dataset
      A collection of :term:`JSONs` for a single conceptual thing. It is also the shared file prefix of the JSONs. For example ``flu/seasonal/h3n2/ha/2y`` identifies a dataset which corresponds to the files
      :

      - ``flu_seasonal_h3n2_ha_2y_meta.json``
      - ``flu_seasonal_h3n2_ha_2y_tree.json``
      - ``flu_seasonal_h3n2_ha_2y_tip-frequencies.json``

      Some workflows produce a single, synonymous dataset, like Zika. Others, like seasonal flu, produce many datasets.

   JSONs
      Special ``.json`` files produced and consumed by :term:`Augur` and visualized by :term:`Auspice`. These files make up a :term:`dataset`.
      See :doc:`data formats<data-formats>`.

   CLI
      also *Nextstrain CLI*

      The Nextstrain command-line interface (**Nextstrain CLI**) provides a consistent way to run and visualize :term:`pathogen builds<Build>` and access Nextstrain components like :term:`Augur` and :term:`Auspice` across :term:`runtimes<runtime>` such as Docker, Native, and AWS Batch.

   runtime
      also *Nextstrain runtime*

      When installing and using Nextstrain, there are different configuration options, or **runtimes**, depending on the operating system.

      1. Docker runtime
      2. Native runtime
      3. AWS Batch runtime (only for ``nextstrain build``)
