=========================
Filtering and Subsampling
=========================

Below are some examples of using :doc:`augur filter <augur:usage/cli/filter>`
and :doc:`augur subsample <augur:usage/cli/subsample>` to sample data.

.. contents:: Table of Contents
   :local:

Overview
========

Augur provides two tools to choose different subsets of input data for various
types of analysis.

- **augur filter**: Tool with command-line configuration options
- **augur subsample**: Tool with file-based configuration options

This guide contains examples for both tools. For ``augur filter`` examples, the options should be added to the following call:

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     <OPTIONS>
     --output-sequences filtered_sequences.fasta \
     --output-metadata filtered_metadata.tsv

For augur subsample examples, the options should be added to a YAML file. If it is named ``samples.yaml``, the following call should be used:

.. code-block:: bash

   augur subsample \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --config samples.yaml \
     --output-sequences filtered_sequences.fasta \
     --output-metadata filtered_metadata.tsv

.. tip::

   Use ``augur filter`` when:

   - You need simple, single-step filtering and subsampling
   - You are comfortable with command-line flags

   Use ``augur subsample`` when:

   - You need complex, multi-tier subsampling (e.g., geographic tiers)
   - You prefer configuration files over long command lines

Options can be categorized based on the selection method.

- **Preliminary** options work by selecting or dropping sequences that match
  certain criteria. Criteria is one of either
  
  1. metadata-based: works with information available from ``--metadata``
  2. sequence-based: works with information available from
     ``--sequences``/``--sequence-index``.

- **Subsampling** options work by selecting sequences using rules based on final
  output size. These are applied after all preliminary options and before any
  force-inclusive options.
- **Force-inclusive** options work by ensuring sequences that match certain
  criteria are always included in the output, ignoring all other options.

.. list-table:: Categories for sampling options
   :header-rows: 1
   :stub-columns: 1

   * -
     - ``augur filter``
     - ``augur subsample``
   * - Preliminary

       (metadata-based)

     - * ``--min-date``
       * ``--max-date``
       * ``--exclude-ambiguous-dates-by``
       * ``--exclude``
       * ``--exclude-where``
       * ``--query``
     - * ``min_date``
       * ``max_date``
       * ``exclude_ambiguous_dates_by``
       * ``exclude``
       * ``exclude_where``
       * ``query``

   * - Preliminary

       (sequence-based)

     - * ``--min-length``
       * ``--max-length``
       * ``--non-nucleotide``
     - * ``min_length``
       * ``max_length``
       * ``non_nucleotide``

   * - Subsampling
     - * ``--subsample-max-sequences``
       * ``--group-by``
       * ``--group-by-weights``
       * ``--sequences-per-group``
       * ``--probabilistic-sampling``
       * ``--no-probabilistic-sampling``
       * ``--priority``
     - * ``max_sequences``
       * ``group_by``
       * ``group_by_weights``
       * ``sequences_per_group``
       * ``probabilistic_sampling``

   * - Force-inclusive
     - * ``--include``
       * ``--include-where``
     - * ``include``
       * ``include_where``

Preliminary & force-inclusive selection
=======================================

A common sampling operation is to select sequences according to rules on
individual sequence attributes. Examples:

- Select all sequences with a collection date in 2012 or later using
  the minimum date option.

  .. list-table::
     :header-rows: 1

     * - ``augur filter`` options
       - ``augur subsample`` config
     * - .. code-block:: bash

            --min-date 2012 \

       - .. code-block:: yaml

            samples:
              my_sample:
                min_date: 2012

- Exclude outliers (e.g. because of sequencing errors, cell-culture adaptation).
  First, create a text file ``exclude.txt`` with one line per sequence ID.

  .. code-block::

      BRA/2016/FC_DQ75D1
      COL/FLR_00034/2015
      ...

  The name of the file is given to the file-based exclusion option.

  .. list-table::
     :header-rows: 1

     * - ``augur filter`` options
       - ``augur subsample`` config
     * - .. code-block:: bash

            --min-date 2012 \
            --exclude exclude.txt \

       - .. code-block:: yaml

            samples:
              my_sample:
                min_date: 2012
                exclude: exclude.txt

- Include sequences from a specific region using the query option.

  .. list-table::
     :header-rows: 1

     * - ``augur filter`` options
       - ``augur subsample`` config
     * - .. code-block:: bash

            --min-date 2012 \
            --exclude exclude.txt \
            --query 'region="Asia"' \

       - .. code-block:: yaml

            samples:
              my_sample:
                min_date: 2012
                exclude: exclude.txt
                query: region="Asia"

  .. tip::

      The query ``region="Asia"`` is functionally equivalent to the column-based
      exclusion ``region!=Asia``. However, the query option allows for more
      complex expressions such as ``(region in {"Asia", "Europe"}) & (coverage
      >= 0.95)``.

      The query ``region="Asia"`` is **not** equivalent to a column-based
      force-inclusion ``region=Asia`` since force-inclusive options ignore other
      options (i.e. minimum date and file-based exclusion in the examples
      above).

Force-inclusive options work similarly, and override all other options.
Example:

- Include specific sequences (e.g. root sequence). First, create a text file
  ``include.txt`` with one line per sequence ID.

  .. code-block::

      Wuhan/Hu-1/2019
      ...

  The name of the file is given to the file-based force-inclusion option.

  .. list-table::
     :header-rows: 1

     * - ``augur filter`` options
       - ``augur subsample`` config
     * - .. code-block:: bash

            --min-date 2020 \
            --include include.txt \

       - .. code-block:: yaml

            samples:
              my_sample:
                min_date: 2020
                include: include.txt

  ``Wuhan/Hu-1/2019`` will still be included even if it does not pass the date filter.

Subsampling
===========

Another common operation is **subsampling**: selection of data using
rules based on output size rather than individual sequence attributes. These are
the sampling methods supported by Augur:

.. contents::
   :local:
   :depth: 2

Random sampling
---------------

The simplest scenario is a reduction of dataset size to more manageable numbers.
For example, limit the output to 100 sequences:

.. list-table::
   :header-rows: 1

   * - ``augur filter`` options
     - ``augur subsample`` config
   * - .. code-block:: bash

          --min-date 2012 \
          --exclude exclude.txt \
          --subsample-max-sequences 100 \

     - .. code-block:: yaml

          samples:
            my_sample:
              min_date: 2012
              exclude: exclude.txt
              max_sequences: 100

Random sampling is easy to define but can expose sampling bias in some datasets.
Consider using grouped sampling to reduce sampling bias.

Grouped sampling
----------------

Grouping columns specified by ``--group-by`` (for ``augur filter``) and
``group_by`` (for ``augur subsample``) allow you to partition the data into
groups based on column values and sample a number of sequences per group.

Grouped sampling can be further divided into two types with a final section for
caveats:

.. contents::
   :local:

Uniform sampling
~~~~~~~~~~~~~~~~

By default (i.e. without weights), Augur will sample uniformly across groups.
For example, sample evenly across regions over time:

.. list-table::
   :header-rows: 1

   * - ``augur filter`` options
     - ``augur subsample`` config
   * - .. code-block:: bash

          --min-date 2012 \
          --exclude exclude.txt \
          --group-by region year month \
          --subsample-max-sequences 100 \

     - .. code-block:: yaml

          samples:
            my_sample:
              min_date: 2012
              exclude: exclude.txt
              group_by:
                - region
                - year
                - month
              max_sequences: 100

An alternative to targeting a total sample size is to target a fixed number of
sequences per group. For example, target one sequence per month from each
region:

.. list-table::
   :header-rows: 1

   * - ``augur filter`` options
     - ``augur subsample`` config
   * - .. code-block:: bash

          --min-date 2012 \
          --exclude exclude.txt \
          --group-by region year month \
          --sequences-per-group 1 \

     - .. code-block:: yaml

          samples:
            my_sample:
              min_date: 2012
              exclude: exclude.txt
              group_by:
                - region
                - year
                - month
              sequences_per_group: 1

Weighted sampling
~~~~~~~~~~~~~~~~~

Weights can be specified in addition to grouping columns to allow different
target sizes per group. For example, target twice the amount of sequences from
Asia compared to other regions using this ``weights.tsv`` file:

.. list-table::
   :header-rows: 1

   * - region
     - weight
   * - Asia
     - 2
   * - default
     - 1

The name of the file is given to the grouping column weights option.

.. list-table::
   :header-rows: 1

   * - ``augur filter`` options
     - ``augur subsample`` config
   * - .. code-block:: bash

          --min-date 2012 \
          --exclude exclude.txt \
          --group-by region year month \
          --group-by-weights weights.tsv \
          --subsample-max-sequences 100 \

     - .. code-block:: yaml

          samples:
            my_sample:
              min_date: 2012
              exclude: exclude.txt
              group_by:
                - region
                - year
                - month
              group_by_weights: weights.tsv
              max_sequences: 100

Multiple grouping columns are supported in the weights file, as well as a
default weight for unspecified groups. A weight of ``0`` can be used to exclude
all matching sequences.

.. list-table::
   :header-rows: 1

   * - region
     - month
     - weight
   * - Asia
     - 2024-01
     - 2
   * - Asia
     - 2024-02
     - 3
   * - Africa
     - 2024-01
     - 2
   * - default
     - default
     - 0

More information can be found in the documentation page for each tool.

Caveats
~~~~~~~

Probabilistic sampling
``````````````````````

It is possible to encounter situations where the number of groups exceeds the
target sample size. For example, consider a command with groups defined by
grouping columns ``region``, ``year``, ``month`` and target sample size of 100
sequences. If the input contains data from 5 regions over a span of 24 months,
that could result in 120 groups.

The only way to target 100 sequences from 120 groups is to apply **probabilistic
sampling** which randomly determines a whole number of sequences per group. This
is noted in the output:

.. code-block:: text

   WARNING: Asked to provide at most 100 sequences, but there are 120 groups.
   Sampling probabilistically at 0.83 sequences per group, meaning it is
   possible to have more than the requested maximum of 100 sequences after
   filtering.

This is automatically enabled. For ``augur filter``,
``--no-probabilistic-sampling`` can be used with uniform sampling to force the
command to exit with an error in these situations. For ``augur subsample``,
``probabilistic_sampling: False`` can be used. It must be enabled for weighted
sampling.

Undersampling
`````````````

For these sampling methods, the number of targeted sequences per group does not
take into account the actual number of sequences available in the input data.
For example, consider a dataset with 200 sequences available from 2023 and 100
sequences available from 2024. When grouping by ``year``, targeting 300 total
sequences is equivalent to targeting 150 sequences per group. This will take 150
sequences from 2023 and all 100 sequences from 2024 for a total of 250
sequences, which is less than the target of 300.

Complex subsampling strategies
==============================

There are some subsampling strategies in which a single call to ``augur filter``
does not suffice or is difficult to create. One such strategy is "tiered
subsampling". In this strategy, mutually exclusive sets of filters, each
representing a "tier", are sampled with different subsampling rules. This is
commonly used to create geographic tiers. In most situations it is recommended
to use ``augur subsample``.

Using ``augur subsample``…
--------------------------

.. contents::
   :local:

.. note::

   ``augur subsample`` is only available in Augur version 31.5.0 and later. If
   you are using an older version of Augur, refer to :ref:`the augur filter
   examples <complex-subsampling-using-augur-filter>`.

… with a dedicated config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following task:

   Sample 200 sequences from Washington state and 100 sequences from the rest of
   the United States.

This can be represented in an ``augur subsample`` config file:

.. code-block:: yaml

   samples:
     state:
       query: state == 'WA'
       max_sequences: 200
     country:
       query: state != 'WA' & country == 'USA'
       max_sequences: 100

… within Snakemake workflow config
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Snakemake`_ is a workflow manager where configuration is often written in YAML
files. A clean pattern is to keep your ``augur subsample`` config inside your
workflow config under a dedicated section, write the ``config`` variable to a YAML
file at run time, and instruct ``augur subsample`` to read from the section.

Consider the following workflow config and ``augur subsample`` usage:

.. code-block:: yaml

   builds:
     build1:
       subsample:
         samples:
           state:
             query: state == 'WA'
             max_sequences: 200
           country:
             query: state != 'WA' & country == 'USA'
             max_sequences: 100

.. code-block:: python

   import yaml
   with open("results/run_config.yaml", "w") as f:
       yaml.dump(config, f, sort_keys=False)

   rule subsample:
       input:
           metadata = "data/metadata.tsv",
           config = "results/run_config.yaml",
       params:
           config_section = ["builds", "build1", "subsample"]
       output:
           metadata = "results/subsampled.tsv",
       shell:
           """
           augur subsample \
             --metadata {input.metadata} \
             --config {input.config} \
             --config-section {params.config_section:q} \
             --output-metadata {output.metadata}
           """

.. tip::

   Quoted interpolations (``:q``) let you include spaces in key names and are
   generally recommended.

Other options (less ideal):

- Maintain a separate YAML dedicated to ``augur subsample``. This is not ideal
  because it splits workflow configuration across files.
- Instruct ``augur subsample`` to read directly from a Snakemake config file.
  This is not ideal because values may be overridden at run time via
  ``--configfile`` or ``--config``. The in-memory ``config`` variable is the
  ultimate source of truth, so writing it out as recommended is more robust.


.. _complex-subsampling-using-augur-filter:

Using ``augur filter``…
-----------------------

.. contents::
   :local:

.. tip::

   Using ``augur subsample`` is recommended for Augur version 31.5.0 and later.

… with weighted sampling
~~~~~~~~~~~~~~~~~~~~~~~~

Consider the following task:

   Sample 200 sequences from Washington state and 100 sequences from the rest of
   the United States.

This can be approximated by first selecting all sequences from the United States
then sampling with these weights:

.. list-table::
    :header-rows: 1

    * - state
      - weight
    * - WA
      - 200
    * - default
      - 2.04

.. code-block:: bash

   augur filter \
     --sequences sequences.fasta \
     --metadata metadata.tsv \
     --query "country == 'USA'" \
     --group-by state \
     --group-by-weights weights.tsv \
     --subsample-max-sequences 300 \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

This approach has some caveats:

1. It relies on a calculation to determine weights, making it less intuitive:

   .. math::

     {n_{\text{other sequences}}} * \frac{1}{{n_{\text{other states}}}}
     =                        100 * \frac{1}{49}
     \approx                 2.04

2. Achieving a full *100 sequences from the rest of the United States* requires
   at least 2 sequences from each of the remaining states. This may not be
   possible if some states are under-sampled.

Intuitiveness for caveat (1) can be improved by adding a comment to the weights
file. However, caveat (2) is an inherent limitation of what is effectively
uniform sampling across all other states. The only way to get around this in
``augur filter`` is **random sampling** across states, but that is not possible
when ``state`` is used as a grouping column.

An alternative approach is to decompose this into multiple schemes, each handled
by a single call to ``augur filter``. Additionally, there is an extra step to
combine the intermediate samples.

   1. Sample 200 sequences from Washington state.
   2. Sample 100 sequences from the rest of the United States.
   3. Combine the samples.

… with multiple calls
~~~~~~~~~~~~~~~~~~~~~

A basic approach is to run the ``augur filter`` commands directly. This works
well for ad-hoc analyses.

.. code-block:: bash

   # 1. Sample 200 sequences from Washington state
   augur filter \
     --sequences sequences.fasta \
     --metadata metadata.tsv \
     --query "state == 'WA'" \
     --subsample-max-sequences 200 \
     --output-strains sample_strains_state.txt
 
   # 2. Sample 100 sequences from the rest of the United States
   augur filter \
     --sequences sequences.fasta \
     --metadata metadata.tsv \
     --query "state != 'WA' & country == 'USA'" \
     --subsample-max-sequences 100 \
     --output-strains sample_strains_country.txt
 
   # 3. Combine using augur filter
   augur filter \
     --sequences sequences.fasta \
     --metadata metadata.tsv \
     --exclude-all \
     --include sample_strains_state.txt \
               sample_strains_country.txt \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

Each intermediate sample is represented by a strain list file obtained from
``--output-strains``. The final step uses ``augur filter`` with ``--exclude-all``
and ``--include`` to sample the data based on the intermediate strain list
files. If the same strain appears in both files, ``augur filter`` will only
write it once in each of the final outputs.

.. note::

   The 2nd sample does not use ``--group-by``, implying **random sampling**
   across states. This differs from previous approach that used a single ``augur
   filter`` command with weighted sampling.

.. _generalizing-subsampling-in-a-workflow:

… generalized within a workflow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The approach above can be cumbersome with more intermediate samples. To
generalize this process and allow for more flexibility, a workflow management
system can be used. The following examples use `Snakemake`_.

1. Add a section in the `config file`_.

   .. code-block:: yaml

      subsampling:
        state: --query "state == 'WA'" --subsample-max-sequences 200
        country: --query "state != 'WA' & country == 'USA'" --subsample-max-sequences 100

2. Add two rules in a `Snakefile`_. If you are building a standard Nextstrain
   workflow, the output files should be used as input to sequence alignment. See
   :doc:`../../learn/parts` to learn more about the placement of
   this step within a workflow.

   .. code-block:: python

      # 1. Sample 200 sequences from Washington state
      # 2. Sample 100 sequences from the rest of the United States
      rule intermediate_sample:
          input:
              metadata = "data/metadata.tsv",
          output:
              strains = "results/sample_strains_{sample_name}.txt",
          params:
              augur_filter_args = lambda wildcards: config.get("subsampling", {}).get(wildcards.sample_name, "")
          shell:
              """
              augur filter \
                  --metadata {input.metadata} \
                  {params.augur_filter_args} \
                  --output-strains {output.strains}
              """
      # 3. Combine using augur filter
      rule combine_intermediate_samples:
          input:
              sequences = "data/sequences.fasta",
              metadata = "data/metadata.tsv",
              intermediate_sample_strains = expand("results/sample_strains_{sample_name}.txt", sample_name=list(config.get("subsampling", {}).keys()))
          output:
              sequences = "results/subsampled_sequences.fasta",
              metadata = "results/subsampled_metadata.tsv",
          shell:
              """
              augur filter \
                  --sequences {input.sequences} \
                  --metadata {input.metadata} \
                  --exclude-all \
                  --include {input.intermediate_sample_strains} \
                  --output-sequences {output.sequences} \
                  --output-metadata {output.metadata}
              """

3. Run Snakemake targeting the second rule.

   .. code-block:: bash

      snakemake combine_intermediate_samples

Explanation:

- The configuration section consists of one entry per intermediate sample in the
  format ``sample_name: <augur filter arguments>``.
- The first rule is run once per intermediate sample using `wildcards`_ and an
  `input function`_. The output of each run is the sampled strain list.
- The second rule uses `expand()`_ to define input as all the intermediate
  sampled strain lists, which are passed directly to ``--include`` as done in
  the previous example.

It is easy to add or remove intermediate samples. The configuration above can be
updated to add another tier in between state and country:

  .. code-block:: yaml

   subsampling:
     state: --query "state == 'WA'" --subsample-max-sequences 100
     neighboring_states: --query "state in {'CA', 'ID', 'OR', 'NV'}" --subsample-max-sequences 75
     country: --query "country == 'USA' & state not in {'WA', 'CA', 'ID', 'OR', 'NV'}" --subsample-max-sequences 50

.. _Snakemake: https://snakemake.readthedocs.io/en/stable/index.html
.. _config file: https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html#snakefiles-standard-configuration
.. _Snakefile: https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html
.. _wildcards: https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#wildcards
.. _input function: https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#snakefiles-input-functions
.. _expand(): https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#the-expand-function
