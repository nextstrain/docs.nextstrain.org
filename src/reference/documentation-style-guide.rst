=========================
Documentation style guide
=========================

This is the (fledgling) style guide for Nextstrain's documentation.


Capitalization
==============

Capitalize the names of our projects, like Nextstrain, Augur, Auspice,
Nextstrain CLI, etc.

Do not capitalize the eponymous commands of our projects, e.g. ``augur``,
``auspice``, ``nextstrain``.


Titles
======

Use short titles in the entries of ``toctree`` directives (i.e. the site
navigation tree) to keep the navigation sidebar easily scannable.  It's ok for
the title of the page itself to be longer/different.


Subprojects
===========

Links
-----

Use Intersphinx references whenever possible for links to our subprojects, e.g.:

.. code-block:: rst

    :doc:`nextstrain build <cli:commands/build>`

Roles other than ``:doc:`` are also supported by Intersphinx.

URLs
----

When you must use a subproject URL instead of an Intersphinx reference—such as
in ``toctree`` directives, documents still using Markdown, and Intersphinx's
configuration—use Read the Docs' `default version redirect`_ (``…/page/…``) to
make sure subproject URLs will always resolve to the subproject's default
version (and language).

For example, do use::

    https://docs.nextstrain.org/projects/cli/page/commands/build/

Do not use::

    https://docs.nextstrain.org/projects/cli/en/stable/commands/build/

This is particularly important for unversioned subprojects (e.g. using
``latest``) which we might start versioning later.

.. _default version redirect: https://docs.readthedocs.io/en/stable/automatic-redirects.html#redirecting-to-a-page
