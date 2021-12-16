========
Glossary
========

.. glossary::

   Augur

      A command-line application used for phylogenetic analysis. :doc:`Documentation<augur:index>`

   Auspice

      A web application used for phylogenetic visualization and analysis. :doc:`Documentation<auspice:index>`

   workflow

      A sequential process producing one or more :term:`datasets<dataset>`, which can be visualized by :term:`Auspice`.

      Our core workflows can be divided into two types:

      1. Single-build workflow (e.g. Zika workflow): one build, one dataset.
      2. Multi-build workflow (e.g. SARS-CoV-2 workflow): multiple builds, multiple datasets.

   build
      also *pathogen build*

      from :doc:`parts of a whole</learn/parts>`

         **Builds** are recipes of code and data that produce result datasets for visualization and analysis.  Builds run dozens of commands and often use `Snakemake <https://snakemake.readthedocs.io>`_ to :doc:`manage the pipeline workflow </guides/bioinformatics/augur_snakemake>`, but any workflow system can be used, such as `Nextflow <https://nextflow.io>`_ or `WDL <https://openwdl.org>`_. As an example, our core builds are organized as `Git repositories <https://git-scm.com>`_ hosted on `GitHub <https://github.com/nextstrain>`_ which contain a Snakemake workflow using Augur, configuration, and data.

      from https://docs.nextstrain.org/projects/augur/en/stable/faq/what-is-a-build.html

         Nextstrain's focus on providing a real-time snapshot of evolving pathogen populations necessitates a reproducible analysis that can be rerun when new sequences are available. The individual steps necessary to repeat analysis together comprise a "build".

         Because no two datasets or pathogens are the same, we build Augur to be flexible and suitable for different analyses. The individual Augur commands are composable, and can be mixed and matched with other scripts as needed. These steps, taken together, are what we refer to as a "build".

      from https://docs.nextstrain.org/projects/ncov/en/latest/analysis/orientation-workflow.html#what-s-a-build

         The components in this diagram constitute a Nextstrain “build” - i.e., a set of commands, parameters and input files which work together to reproducibly execute bioinformatic analyses and generate a JSON for visualization with auspice. You can learn more about builds `here <https://docs.nextstrain.org/projects/ncov/en/latest/analysis/orientation-workflow.html#what-s-a-build>`_.

         Builds are particularly important if you frequently want to run several different analysis workflows or datasets. For example, if you wanted to run one analysis on just your data and another analysis that incorporates background / contextual sequences, you could configure two different builds (one for each of these workflows). We'll cover this in more detail in the `basic build configuration <https://docs.nextstrain.org/projects/ncov/en/latest/analysis/running.html>`_ section.

      from https://github.com/nextstrain/nextstrain.org/blob/master/docs/glossary.md#build

         A *build* is a collection of data and code that produces :term:`datasets<dataset>` for visualization on nextstrain.org.
         Our [core](#core) builds — for example `Zika <https://github.com/nextstrain/zika>`_ — are organized as git repositories hosted on GitHub which contain a `Snakemake <https://snakemake.readthedocs.io>`_ workflow using :term:`Augur`, configuration, and data.
         Builds produce :term:`JSONs` which can be visualized by :term:`Auspice` and may be deployed to Nextstrain.

   build step
      also *pathogen build step*

      A modular instruction of a :term:`build` which can be run standalone (e.g. ``augur filter``), often with clear input and output files.

   build script
      also *pathogen build script*

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
