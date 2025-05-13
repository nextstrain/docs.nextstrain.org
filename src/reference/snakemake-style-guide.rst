=====================
Snakemake style guide
=====================

When in doubt, refer to `Snakemake's own best practices
guide <https://snakemake.readthedocs.io/en/stable/snakefiles/best_practices.html>`__.

.. contents:: Table of Contents
   :local:

Avoid ``run`` blocks
====================

Instead, implement custom Python in scripts called in a ``shell`` block.

-  Code in ``run`` blocks is less reusable. Anything we write once,
   we're likely to want to reuse later.

-  ``run`` blocks can be challenging to debug.

-  ``run`` blocks do not run in rule-specific conda environments,
   forcing the user to manually install into their environment any
   dependencies that could have been in a conda environment file.

Define ``input`` paths with literal path strings
================================================

Do this instead of using ``rule`` variables.

-  Literal paths are easier to read and interpret, avoiding the need to
   trace back through a workflow to an earlier rule to see the path
   associated with a rule output.

-  Literal paths also allow workflows to be rewired with custom rules
   that are injected at runtime. For example, `the ncov workflow allows
   users to define their own rules
   <https://docs.nextstrain.org/projects/ncov/en/latest/reference/configuration.html#custom-rules>`__
   that can provide alternate commands for generating required files.
   This approach does not work with references to rule outputs, though
   (`see ncov PR 877 <https://github.com/nextstrain/ncov/pull/877>`__,
   for an example).

Always use relative paths
=========================

Relative paths (paths that don't start with ``/``) mean that anyone can
run the build without running into portability issues caused by paths
specific to your computer.

See the `Snakemake documentation
<https://snakemake.readthedocs.io/en/stable/project_info/faq.html#how-does-snakemake-interpret-relative-paths>`__
for how relative paths are interpreted depending on context.

Avoid the ``message`` rule attribute
====================================

When the ``message`` attribute is defined, Snakemake suppresses other critical
details that otherwise get displayed by default (e.g., job id, rule name,
input, output, etc.).

Use a YAML configuration file and allow for overrides
=====================================================

Configuration is data and should live inside YAML files. By including the
following snippet in your Snakefile, you can provide default values and allow
for additional entries or overrides via the ``--configfile`` or ``--config``
options to ``snakemake``.

.. code-block:: python

   configfile: "defaults.yaml"

Configuration values are available as a ``config`` dictionary provided in scope
afterwards.

Access ``config`` values appropriately
======================================

Use the appropriate method to access configuration in the ``config``
global variable. 3 ways are supported, but only 2 should be used:

1. ``config[key]``: Use this when the key is required, or a default is
   specified in a pre-loaded configuration file.

2. ``key [not] in config``: Use this when the key is optional and you
   want to check if a value is specified.

3. ``config.get(key, default)``: Use this when the key is optional and
   you want to access its value.

4. ``config.get(key)``: **Never use this**. All use cases should be covered
   by the options above. Using this will only mask errors that may be
   due to a missing required key.

Use Snakemake ``params:`` block to map into ``config`` dictionary
=================================================================

For example, do this:

.. code-block:: python

   params:
       name = lambda _: config["name"]
   shell:
       r"""
       echo {params.name:q}
       """

instead of using the ``config`` dictionary directly in the shell
command. This has several benefits:

-  Interpolation of dictionary lookups in the shell commands is
   non-standard and confusing. (You have to use ``{config[name]}``, for
   example. Note that the dictionary key is unquoted.)

-  Param definitions can use arbitrary Python expressions, so you can do
   more complicated things than you can with direct interpolation, such
   as list comprehensions.

-  Snakemake can automatically discover which rules have parameter
   values that are different than the last run and show what output
   files are affected (``--list-params-changes``).

Use lambda on ``params`` that may have ``{`` or ``}`` in the value
==================================================================

If the value passed to a param contains curly braces, Snakemake will attempt to
resolve it as a wildcard. To keep the value as-is, `use a lambda expression <https://github.com/snakemake/snakemake/issues/2166#issuecomment-1464202922>`__.

Example:

.. code-block:: python

   params:
       key=lambda w: config["value_may_contain_curlies"]

Always use quoted (:q) interpolations
=====================================

When building shell commands to run, Snakemake does not by default
properly quote interpolated values. This works fine if the interpolated
value doesn't contain spaces or other special shell metacharacters (like
quotes or backslashes), but it is fragile and a time-bomb waiting to
break on future values.

Standard best practice in any language or environment is to always quote
parameters in generated shell commands. Snakemake supports this using
the ``:q`` modifier for interpolation:

.. code-block:: python

   params:
       file = "filename with spaces.txt"
   shell:
       r"""
       wc -l {params.file:q}
       """

Not quoting these values is also a security risk.

It may be tempting to make an exception for parameters with multiple
values where you want each become a separate command-line argument, such
as a parameter listing three filenames. In this case, however, it's
recommended that you make the parameter a list instead of a single
string. Snakemake will interpolate it correctly:

.. code-block:: python

   params:
       files = ["a.txt", "b.txt", "c.txt"]
   shell:
       r"""
       wc -l {params.files:q}
       """

.. _use-triple-quoted-command-definitions:

Use raw, triple-quoted shell blocks
===================================

Using raw, triple-quoted (``r"""`` or ``r'''``) ``shell`` blocks makes it
much easier to build readable commands with one-option per line. It also
avoids any nested quoting issues if you need to use literal single or
double quotes in your command. The command will remain readable in
Snakemake's logging messages because it'll look like the source form
(e.g. with backslashes and newlines retained instead of collapsed).

Example:

.. code-block:: python

   shell:
       r"""
       augur parse \
           --sequences {input:q} \
           --fields {params.fields:q} \
           --output-sequences {output.sequences:q} \
           --output-metadata {output.metadata:q}
       """

.. hint::
    If you're converting interpreted strings to raw strings (e.g.
    ``"""`` to ``r"""``), make sure to check that they're not relying on
    `escape sequences`_ like ``\n``, ``\t``, or ``\\`` to be interpreted by
    Python before the shell (Bash) sees them.

.. _escape sequences: https://docs.python.org/3/reference/lexical_analysis.html#escape-sequences

Log standard out and error output to log files and the terminal
===============================================================

Use `the Snakemake log directive <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#log-files>`_ for each rule that writes output to either standard out or error and direct output to the corresponding log file.
Use the ``tee`` command to ensure that output gets written to both the log file and the terminal, so users can track their workflow progress interactively and use the log file later for debugging.
Use ``exec`` to capture output from the entire shell block, which is useful if there are multiple commands (e.g. piping).

Example:

.. code-block:: python

   log:
       "logs/filter.txt"
   shell:
       r"""
       exec &> >(tee {log:q})

       augur filter \
           --metadata {input.metadata:q} \
           --output-metadata {output.metadata:q}
       """

Before using ``tee``, ensure that your workflow uses `bash's pipefail option <http://redsymbol.net/articles/unofficial-bash-strict-mode/>`_, so successful ``tee`` execution does not mask errors from earlier commands in the pipe.
Snakemake uses bash's strict mode by default, so the pipefail option should be enabled by default.
However, some workflows may override the defaults `locally at specific rules <https://snakemake.readthedocs.io/en/stable/project_info/faq.html#my-shell-command-fails-with-exit-code-0-from-within-a-pipe-what-s-wrong>`_ or globally as with `a custom shell prefix <https://github.com/nextstrain/ncov/pull/751>`_.

Run workflows with ``--show-failed-logs``
=========================================

Run workflows with the ``--show-failed-logs`` which will print the logs for failed jobs to the terminal when the workflow exits.
This pattern helps users identify error messages without first finding the corresponding log file.

Always use the ``benchmark`` directive
======================================

Use `the Snakemake benchmark directive <https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#benchmark-rules>`_
for each rule so that it is easy to track run time and memory usage.
This makes it easier for us identify bottlenecks in workflows without parsing Snakemake logs.
