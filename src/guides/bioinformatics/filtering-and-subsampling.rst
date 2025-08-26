=========================
Filtering and Subsampling
=========================

Below are some examples of using :doc:`augur filter <augur:usage/cli/filter>`
and :doc:`augur subsample <augur:usage/cli/subsample>` to sample data.

.. contents:: Table of Contents
   :local:

Overview
========

``augur filter`` provides the flexibility to choose different subsets of input
data for various types of analysis. There are several options which can be
categorized based on the information source and selection method.

Information source:

- **Metadata-based** options work with information available from
  ``--metadata``.
- **Sequence-based** options work with information available from
  ``--sequences`` or ``--sequence-index``.

Selection method:

- **Preliminary** options work by selecting or dropping sequences that match
  certain criteria.
- **Subsampling** options work by selecting sequences using rules based on final
  output size. These are applied after all preliminary options and before any
  force-inclusive options.
- **Force-inclusive** options work by ensuring sequences that match certain
  criteria are always included in the output, ignoring all other filter options.

.. list-table:: Categories for filter options
   :header-rows: 1
   :stub-columns: 1

   * -
     - Metadata-based
     - Sequence-based
   * - Preliminary
     - * ``--min-date``
       * ``--max-date``
       * ``--exclude-ambiguous-dates-by``
       * ``--exclude``
       * ``--exclude-where``
       * ``--query``
     - * ``--min-length``
       * ``--max-length``
       * ``--non-nucleotide``

   * - Subsampling
     - * ``--subsample-max-sequences``
       * ``--group-by``
       * ``--group-by-weights``
       * ``--sequences-per-group``
       * ``--probabilistic-sampling``
       * ``--no-probabilistic-sampling``
       * ``--priority``
     - *None*

   * - Force-inclusive
     - * ``--include``
       * ``--include-where``
     - *None*

Preliminary & force-inclusive selection
=======================================

A common filtering operation is to select sequences according to rules on
individual sequence attributes. Examples:

- Select all sequences with a collection date in 2012 or later using
  ``--min-date 2012``:

  .. code-block:: bash

     augur filter \
       --sequences data/sequences.fasta \
       --metadata data/metadata.tsv \
       --min-date 2012 \
       --output-sequences filtered_sequences.fasta \
       --output-metadata filtered_metadata.tsv

- Exclude outliers (e.g. because of sequencing errors, cell-culture adaptation)
  using ``--exclude``. First, create a text file ``exclude.txt`` with one line
  per sequence ID:

  .. code-block::

      BRA/2016/FC_DQ75D1
      COL/FLR_00034/2015
      ...

  Add the option by using ``--exclude exclude.txt`` in the command:

  .. code-block:: bash

      augur filter \
        --sequences data/sequences.fasta \
        --metadata data/metadata.tsv \
        --min-date 2012 \
        --exclude exclude.txt \
        --output-sequences filtered_sequences.fasta \
        --output-metadata filtered_metadata.tsv

- Include sequences from a specific region using ``--query``:

  .. code-block:: bash

      augur filter \
        --sequences data/sequences.fasta \
        --metadata data/metadata.tsv \
        --min-date 2012 \
        --exclude exclude.txt \
        --query 'region="Asia"' \
        --output-sequences filtered_sequences.fasta \
        --output-metadata filtered_metadata.tsv

  .. tip::

      ``--query 'region="Asia"'`` is functionally equivalent to ``--exclude-where
      region!=Asia``. However, ``--query`` allows for more complex expressions such
      as ``--query '(region in {"Asia", "Europe"}) & (coverage >= 0.95)'``.

      ``--query 'region="Asia"'`` is **not** equivalent to ``--include-where
      region=Asia`` since force-inclusive options ignore other filter options
      (i.e. ``--min-date`` and ``--exclude`` in the example above).

Force-inclusive options work similarly, and override all other filtering
options. Example:

- Include specific sequences (e.g. root sequence) using ``--include``. First,
  create a text file ``include.txt`` with one line per sequence ID:

  .. code-block::

      Wuhan/Hu-1/2019
      ...

  Add the option by using ``--include include.txt`` in the command:

  .. code-block:: bash

      augur filter \
        --sequences data/sequences.fasta \
        --metadata data/metadata.tsv \
        --min-date 2020 \
        --include include.txt \
        --output-sequences filtered_sequences.fasta \
        --output-metadata filtered_metadata.tsv

  ``Wuhan/Hu-1/2019`` will still be included even if it does not pass the filter
  ``--min-date 2020``.

Subsampling
===========

Another common filtering operation is **subsampling**: selection of data using
rules based on output size rather than individual sequence attributes. These are
the sampling methods supported by ``augur filter``:

.. contents::
   :local:
   :depth: 2

Random sampling
---------------

The simplest scenario is a reduction of dataset size to more manageable numbers.
For example, limit the output to 100 sequences:

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --min-date 2012 \
     --exclude exclude.txt \
     --subsample-max-sequences 100 \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

Random sampling is easy to define but can expose sampling bias in some datasets.
Consider using grouped sampling to reduce sampling bias.

Grouped sampling
----------------

``--group-by`` allows you to partition the data into groups based on column
values and sample a number of sequences per group.

Grouped sampling can be further divided into two types with a final section for
caveats:

.. contents::
   :local:

Uniform sampling
~~~~~~~~~~~~~~~~

By default (i.e. without ``--group-by-weights``), ``--group-by`` will sample
uniformly across groups. For example, sample evenly across regions over time:

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --min-date 2012 \
     --exclude exclude.txt \
     --group-by region year month \
     --subsample-max-sequences 100 \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

An alternative to ``--subsample-max-sequences`` is ``--sequences-per-group``.
This is useful if you care less about total sample size and more about having
a fixed number of sequences from each group. For example, target one sequence
per month from each region:

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --min-date 2012 \
     --exclude exclude.txt \
     --group-by region year month \
     --sequences-per-group 1 \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

Weighted sampling
~~~~~~~~~~~~~~~~~

``--group-by-weights`` can be specified in addition to ``--group-by`` to allow
different target sizes per group. For example, target twice the amount of
sequences from Asia compared to other regions using this ``weights.tsv`` file:

.. list-table::
   :header-rows: 1

   * - region
     - weight
   * - Asia
     - 2
   * - default
     - 1

and command:

.. code-block:: bash

   augur filter \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --min-date 2012 \
     --exclude exclude.txt \
     --group-by region year month \
     --group-by-weights weights.tsv \
     --subsample-max-sequences 100 \
     --output-sequences subsampled_sequences.fasta \
     --output-metadata subsampled_metadata.tsv

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

More information can be found in ``augur filter`` docs for
``--group-by-weights``.

Caveats
~~~~~~~

Probabilistic sampling
``````````````````````

It is possible to encounter situations where the number of groups exceeds the
target sample size. For example, consider a command with groups defined by
``--group-by region year month`` and target sample size defined by
``--subsample-max-sequences 100``. If the input contains data from 5 regions
over a span of 24 months, that could result in 120 groups.

The only way to target 100 sequences from 120 groups is to apply **probabilistic
sampling** which randomly determines a whole number of sequences per group. This
is noted in the output:

.. code-block:: text

   WARNING: Asked to provide at most 100 sequences, but there are 120 groups.
   Sampling probabilistically at 0.83 sequences per group, meaning it is
   possible to have more than the requested maximum of 100 sequences after
   filtering.

This is automatically enabled. ``--no-probabilistic-sampling`` can be used with
uniform sampling to force the command to exit with an error in these situations.
It is always be enabled for weighted sampling.

Undersampling
`````````````

For these sampling methods, the number of targeted sequences per group does not
take into account the actual number of sequences available in the input data.
For example, consider a dataset with 200 sequences available from 2023 and 100
sequences available from 2024. ``--group-by year --subsample-max-sequences 300``
is equivalent to ``--group-by year --sequences-per-group 150``. This will take
150 sequences from 2023 and all 100 sequences from 2024 for a total of 250
sequences, which is less than the target of 300.

Complex subsampling strategies
==============================

There are some subsampling strategies in which a single call to ``augur filter``
does not suffice or is difficult to create. One such strategy is "tiered
subsampling". In this strategy, mutually exclusive sets of filters, each
representing a "tier", are sampled with different subsampling rules. This is
commonly used to create geographic tiers.

Using ``augur subsample``
-------------------------

.. note::

   ``augur subsample`` is only available in Augur version 31.5.0 and later. If
   you are using an older version of Augur, refer to :ref:`the augur filter
   examples <complex-subsampling-using-augur-filter>`.

In most situations it is recommended to use ``augur subsample``. Consider the following task:

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

If it is named ``samples.yaml``, the following call should be used:

.. code-block:: bash

   augur subsample \
     --sequences data/sequences.fasta \
     --metadata data/metadata.tsv \
     --config samples.yaml \
     --output-sequences filtered_sequences.fasta \
     --output-metadata filtered_metadata.tsv


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
