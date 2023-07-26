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

Avoid the ``message`` rule attribute
====================================

-  When the ``message`` attribute is defined, Snakemake suppresses other
   critical details that otherwise get displayed by default (e.g., job
   id, rule name, input, output, etc.).

Access ``config`` values appropriately
======================================

Use the appropriate method to access configuration in the ``config``
global variable. 3 ways are supported, but only 2 should be used:

1. ``config[key]``: Use this when the key is required, or a default is
   specified in a pre-loaded configuration file.

2. ``config.get(key, default)``: Use this when the key is optional.

3. ``config.get(key)``: Never use this. All use cases should be covered
   by (1) and (2). Using this will only mask errors that may be due to a
   missing required key.

Use lambda on ``params`` that may have ``{`` or ``}`` in the value
==================================================================

If the value passed to a param contains curly braces, Snakemake will attempt to
resolve it as a wildcard. To keep the value as-is, `use a lambda expression <https://github.com/snakemake/snakemake/issues/2166#issuecomment-1464202922>`__.

Example:

.. code-block:: python

   params:
       key=lambda w: config["value_may_contain_curlies"]

Use a config.yaml file
======================

Configuration is data and should live inside a YAML file named
``config.yaml``. You can access it in your Snakefile by including the
line:

.. code-block:: python

   configfile: "config.yaml"

and then using the ``config`` dictionary provided in scope afterwards.

Allow for easy config overrides
===============================

By including the following snippet in your Snakefile, you can allow for
optional configuration overrides using the ``--configfile`` option to
``snakemake``.

.. code-block:: python

   if not config:
       configfile: "config.yaml"

Use Snakemake ``params:`` block to map into ``config`` dictionary
=================================================================

For example, do this:

.. code-block:: python

   params:
       name = config["name"]
   shell:
       "echo {params.name:q}"

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
       "wc -l {params.file:q}"

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
       "wc -l {params.files:q}"

Use triple-quoted command definitions
=====================================

Using triple-quoted (``"""`` or ``'''``) command definitions make it
much easier to build readable commands with one-option per line. It also
avoids any nested quoting issues if you need to use literal single or
double quotes in your command.

Example:

.. code-block:: python

   shell:
       """
       augur parse \
           --sequences {input:q} \
           --fields {params.fields:q} \
           --output-sequences {output.sequences:q} \
           --output-metadata {output.metadata:q}
       """

Always use relative paths
=========================

Relative paths (paths that don't start with ``/``) mean that anyone can
run the build without running into portability issues caused by paths
specific to your computer.

See the `Snakemake documentation
<https://snakemake.readthedocs.io/en/stable/project_info/faq.html#how-does-snakemake-interpret-relative-paths>`__
for how relative paths are interpreted depending on context.
