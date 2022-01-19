========
Glossary
========

.. glossary::

   Augur

      A command-line application used for phylogenetic analysis. :doc:`Documentation<augur:index>`

   Auspice

      A web application used for phylogenetic visualization and analysis. :doc:`Documentation<auspice:index>`

   workflow
      also *pathogen workflow*, *pathogen analysis*, *Nextstrain workflow*

      A reproducible process comprised of one or more :term:`builds<build>` producing :term:`datasets<dataset>`, which can be visualized by :term:`Auspice`. Implementation varies per workflow, but generally they are run by workflow managers such as Snakemake.

      Our :term:`core workflows<core workflow>` can be divided into two types:

      1. Single-build workflow (e.g. Zika workflow): one build producing one dataset.
      2. Multi-build workflow (e.g. SARS-CoV-2 workflow): multiple builds producing multiple datasets.

      .. note::

         The individual builds in a multi-build workflow are also "workflows" in the definition of workflow managers like Snakemake.

   core workflow

      A :term:`workflow` maintained by the Nextstrain team.

   workflow repository
      also *pathogen workflow repository*

      A version-controlled folder containing all files necessary to run a :term:`workflow`.

   build
      also *Nextstrain build*

      *(noun)* A sequence of commands, parameters and input files which work together to reproducibly execute bioinformatic analyses and generate a :term:`dataset` for visualization with :term:`Auspice`.

   build (verb)

      A general term for running a :term:`workflow` (e.g. ``nextstrain build``).

   build step

      A modular instruction of a :term:`build` which can be run standalone (e.g. ``augur filter``), often with clear input and output files.

   dataset
      also *Auspice JSONs*

      A collection of :term:`JSONs` produced by a :term:`build`. It is also the shared file prefix of the JSONs. For example ``flu/seasonal/h3n2/ha/2y`` identifies a dataset which corresponds to the files
      :

      - ``flu_seasonal_h3n2_ha_2y_meta.json``
      - ``flu_seasonal_h3n2_ha_2y_tree.json``
      - ``flu_seasonal_h3n2_ha_2y_tip-frequencies.json``

      Some :term:`workflows<workflow>` produce a single, synonymous dataset, like Zika. Others, like seasonal flu, produce many datasets.

   narrative

      A method of data-driven storytelling with interactive views of :term:`datasets <dataset>` displayed alongside multiple pages (or slides) of text and images.
      Saved as a Markdown file with extended syntax to support additional displays.

      Viewable on nextstrain.org or with :term:`Auspice` via the :doc:`cli:commands/view` or :doc:`auspice view <auspice:introduction/how-to-run>` commands.

      See also :doc:`/guides/communicate/narratives-intro` and :doc:`/tutorials/narratives-how-to-write`.

   JSONs
      Special ``.json`` files produced by :term:`Augur` and visualized by :term:`Auspice`. These files make up a :term:`dataset`.
      See :doc:`data formats<data-formats>`.

   CLI
      also *Nextstrain CLI*

      The Nextstrain command-line interface (**Nextstrain CLI**) provides a consistent way to run and visualize :term:`pathogen builds<Build>` and access Nextstrain components like :term:`Augur` and :term:`Auspice` across :term:`runtimes<runtime>` such as Docker, Native, and AWS Batch.

      :doc:`Documentation <cli:index>`

   runtime
      also *Nextstrain runtime*

      When installing and using the :term:`Nextstrain CLI<CLI>`, there are different configuration options, or **runtimes**, depending on the operating system.

      1. Docker runtime
      2. Native runtime
      3. AWS Batch runtime (only for ``nextstrain build``)
