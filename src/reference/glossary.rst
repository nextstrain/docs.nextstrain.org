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

      A reproducible process producing one or more :term:`datasets<dataset>`, which can be visualized by :term:`Auspice`. Implementation varies per workflow, but generally they are run by workflow managers such as Snakemake.

   core workflow

      A :term:`workflow` maintained by the Nextstrain team.

   workflow repository
      also *pathogen workflow repository*

      A version-controlled folder containing all files necessary to run a :term:`workflow`.

   build (verb)

      A general term for running a :term:`workflow` (e.g. ``nextstrain build``).

   dataset
      also *Auspice JSONs, Nextstrain dataset*

      A collection of :term:`JSONs` produced by a :term:`workflow`. It is also the shared file prefix of the JSONs. For example ``flu/seasonal/h3n2/ha/2y`` identifies a dataset which corresponds to the files
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

   Nextstrain CLI

      The Nextstrain command-line interface (**Nextstrain CLI**) provides a consistent way to run and visualize :term:`pathogen workflows<workflow>` and access Nextstrain components like :term:`Augur` and :term:`Auspice` across :term:`runtimes<runtime>` such as Docker, Native, and AWS Batch.

      :doc:`Documentation <cli:index>`

   runtime
      also *Nextstrain runtime*

      When installing and using the :term:`Nextstrain CLI`, there are different configuration options, or **runtimes**, depending on the operating system.

      1. Docker runtime
      2. Native runtime
      3. AWS Batch runtime (only for ``nextstrain build``)
