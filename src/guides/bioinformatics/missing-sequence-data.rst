===============================================
Missing sequence data (gaps, indels, ambiguity)
===============================================

It's common for genome sequences to be incomplete in some way. This could be due to low sequence coverage,
regions which were hard to map / assemble, or simply a by-product of the sequencing approach used.
Typically regions of low coverage / sequence-drop-out / ambiguity are represented by "N" in
the (consensus) sequence. This differs from deletions which are represented by the "-" gap character.
Unfortunately this approach is not applied consistently across bioinformatics tools, and thus knowing
whether a gap is a true insertion (or vice versa) requires knowledge of the assembly / mapping approach
used, access to the raw data (e.g. FASTQ files), or using a heuristic approach [#f1]_.

This document summarises how certain character classes are affected as different Augur commands are run.
For specific behaviour of each command you can refer to the documentation covering the
:doc:`augur subcommands <augur:usage/cli/cli>`.


Invalid characters
==================

An invalid character is any not in the following set (case insensitive):
``{"A", "G", "C", "T", "U", "N", "R", "Y", "S", "W", "K", "M", "B", "V", "D", "H", "-"}``.
:doc:`augur filter <augur:usage/cli/filter>` can remove sequences entirely if they have
invalid characters via the ``--non-nucleotide`` argument, and :doc:`augur mask <augur:usage/cli/mask>`
can replace invalid characters with "N" via ``--mask-invalid`` (not the default, but recommended).
Different aligners may modify such characters, however MAFFT (the default for
:doc:`augur align <augur:usage/cli/align>`) will leave them unchanged.

Invalid characters which remain will be reported as "N" by
:doc:`augur ancestral <augur:usage/cli/ancestral>`, and thus not be visible in Auspice as mutations.

Ambiguous characters
====================

These characters behave differently when inferring mutations across the tree via
:doc:`augur ancestral <augur:usage/cli/ancestral>`. The default behaviour is to infer the actual
base at that position (default behaviour is the same as using the ``--infer-ambiguous`` argument).
You can avoid this by using the ``--keep-ambiguous``.

For instance, if a parent node has "G" and a child node has "R" (an ambiguous character
representing a purine) then the default behaviour would be to infer the "R" is a "G" and thus
there is no mutation. Using ``--keep-ambiguous`` we instead report a G→N change, which
when viewed in Auspice will be reported as Ns, separately to mutations.

"N" characters (missing data)
==============================

When mutations are inferred using :doc:`augur ancestral <augur:usage/cli/ancestral>`, the behaviour of
"N" is similar to ambiguous characters. For example, if a parent node has "G" and a child node
has "N" then the default behaviour would be to infer the "N" as a "G" and thus report no mutation.
Using ``--keep-ambiguous`` we instead report a G→R mutation.

This behaviour is also described in the table below.

Gap characters
==============

As mentioned above, gap characters may represent true gaps but they commonly also represent unknown nucleotides;
Augur is designed around the former (correct) interpretation, and it is worth scanning your data to check
how these characters are being used.

:doc:`augur align <augur:usage/cli/align>` has the ability to replace all gaps with "N"s using the
``--fill-gaps`` argument.


Gap characters are treated differently by :doc:`augur ancestral <augur:usage/cli/ancestral>` depending on
whether they appear in terminal regions or not, due to aligners introducing gaps at the start
and end of sequences if they are not fully complete (which is very common). This behaviour can be removed
by using ``--keep-overhangs``. Note that the ``--infer-ambiguous`` argument is the default, but is listed
here to make things explicit, and we also describe the behaviour of Ns to compare and contrast.

+--------------------------------------+-----------------+-----------------+-----------------+
|``augur ancestral`` behaviour for     | terminal gaps   | internal gaps   |  N              |
+======================================+=================+=================+=================+
|``--infer-ambiguous``                 | Nuc inferred    | Reported as gap | Nuc inferred    |
+--------------------------------------+-----------------+-----------------+-----------------+
|``--keep-ambiguous``                  | Reported as Ns  | Reported as gap | Reported as Ns  |
+--------------------------------------+-----------------+-----------------+-----------------+
|``--infer-ambiguous --keep-overhangs``| Reported as gap | Reported as gap | Nuc inferred    |
+--------------------------------------+-----------------+-----------------+-----------------+
|``--keep-ambiguous  --keep-overhangs``| Reported as gap | Reported as gap | Reported as Ns  |
+--------------------------------------+-----------------+-----------------+-----------------+


Censor particular regions or positions
======================================

The above sections have focused on the behaviour of specific characters in sequences as they
move through Augur commands, however :doc:`augur mask <augur:usage/cli/mask>` also has the ability
to replace pre-defined positions or terminal regions with "N"s, no matter what their contents.

--------------

.. rubric:: Footnotes

.. [#f1] As an example, around a third of SARS-CoV-2 sequences have gap characters but no
  "N"s, an improbable situation which we believe to be a bioinformatic artifact.
