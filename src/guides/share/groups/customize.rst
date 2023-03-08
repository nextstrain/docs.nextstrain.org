.. _group-customization:

===========================
Customize your group's page
===========================

You can customize the content of your group's page thru two files:

:file:`group-overview.md`
    A title, byline, website, and/or description of your group.  Displayed at the top of your group's splash page.

:file:`group-logo.png`
    A logo for your group.  Displayed at the top of your group's splash page.

The names of these files do not matter, so you may use whatever makes most sense to to you.
This guide will use the names above in examples.

.. note::
    This guide currently uses ``curl`` to make direct API requests.  In the
    future, there will be a web interface for managing your group's
    customizations (and possibly also Nextstrain CLI commands).

Log in with the Nextstrain CLI
==============================

Before you can customize your group's page, you need to log into nextstrain.org with the Nextstrain CLI's :doc:`cli:commands/login` command so we can use its :doc:`cli:commands/authorization` command::

    nextstrain login

Confirm that you have access to your group by running :doc:`cli:commands/whoami`::

    nextstrain whoami

You should see your group name in the output.
You must have the :term:`owners role <owners>` within a group to change its customizations.

Adding
======

Create a new file named :file:`group-overview.md` that will contain information about your group:

.. code-block:: yaml

   ---
   title: "Your Department of Health and Human Services"
   byline: "Your Name Here"
   website: https://
   showDatasets: true
   showNarratives: true
   ---

   A description of your organization goes here.

The top of this file provides a title for the page, a list of people who maintain the data, a website, and/or whether to show datasets and narratives from your group.
This information is technically known as the `YAML front matter <https://jekyllrb.com/docs/front-matter/>`__ for the file.

All fields are optional and either have generic defaults (like the title) or are omitted from the page by default (like the byline and website link).
Dataset and narrative listings are both shown (i.e. ``true``) by default if not specified otherwise in this file with a value of ``false``.

After the front matter (in the lines following the last ``---`` characters), write a description of your organization to provide context for users who can access your groups page.
Use `Markdown syntax <https://www.markdownguide.org/basic-syntax/>`__ to format the contents of your group description with headers, lists, links, etc.
This content will appear between the title/byline/website heading and the list of available datasets on the group's page.

.. highlight:: bash

.. role:: bash(code)
   :language: bash

With this :file:`group-overview.md` file, you can now update your group's overview settings::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/overview \
        --header @<(nextstrain authorization) \
        --header "Content-Type: text/markdown" \
        --upload-file group-overview.md

Make sure to replace :bash:`${GROUPNAME}` with your group's actual name.

If you have a logo image in `PNG format <https://en.wikipedia.org/wiki/PNG>`__, you can use that too::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/logo \
        --header @<(nextstrain authorization) \
        --header "Content-Type: image/png" \
        --upload-file group-logo.png

Changing
========

Edit your local files and repeat the ``curl`` commands above to make changes to your existing customizations.

If you no longer have the customization files locally, you can download the :file:`group-overview.md` file::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/overview \
        --header @<(nextstrain authorization) \
        --header "Accept: text/markdown" \
        > group-overview.md

and/or the :file:`group-logo.png` file::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/logo \
        --header @<(nextstrain authorization) \
        --header "Accept: image/png" \
        > group-logo.md

Removing
========

To remove the overview customizations::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/overview \
        --header @<(nextstrain authorization) \
        --request DELETE

and/or the logo::

    curl -fsS https://nextstrain.org/groups/${GROUPNAME}/settings/logo \
        --header @<(nextstrain authorization) \
        --request DELETE
