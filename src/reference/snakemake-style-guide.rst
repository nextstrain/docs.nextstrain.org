=====================
Snakemake style guide
=====================

When in doubt, refer to `Snakemake's own best practices
guide <https://snakemake.readthedocs.io/en/stable/snakefiles/best_practices.html>`__.

-  Avoid ``run`` blocks; implement custom Python in scripts called in a
   ``shell`` block.

   -  Code in ``run`` blocks is less reusable. Anything we write once,
      we're likely to want to reuse later.

   -  ``run`` blocks can be challenging to debug.

   -  ``run`` blocks do not run in rule-specific conda environments,
      forcing the user to manually install into their environment any
      dependencies that could have been in a conda environment file.

-  Define ``input`` paths with literal path strings instead of ``rule``
   variables.

   -  Literal paths are easier to read and interpret, avoiding the need
      to trace back through a workflow to an earlier rule to see the
      path associated with a rule output.

   -  Literal paths also allow workflows to be rewired with custom rules
      that are injected at runtime. For example, `the ncov workflow
      allows users to define their own
      rules <https://docs.nextstrain.org/projects/ncov/en/latest/reference/configuration.html#custom-rules>`__
      that can provide alternate commands for generating required files.
      This approach does not work with references to rule outputs,
      though (`see ncov PR
      877 <https://github.com/nextstrain/ncov/pull/877>`__, for an
      example).

-  Avoid the ``message`` rule attribute.

   -  When the ``message`` attribute is defined, Snakemake suppresses
      other critical details that otherwise get displayed by default
      (e.g., job id, rule name, input, output, etc.).
