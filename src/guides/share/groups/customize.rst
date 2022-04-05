.. _group-customization:

===========================
Customize your group's page
===========================

.. hint::
    This guide currently only applies to :doc:`Nextstrain Groups
    </learn/groups/index>` which have not yet :doc:`migrated from S3
    <migrate-from-s3>`.

    We'll update this page once self-service customization is restored for
    groups that have migrated.  In the meantime, please `email us`__ if you
    need to update your group's customizations.

    __ mailto:hello@nextstrain.org?subject=Group%20customizations%20request

You can customize the content of your group's page by uploading two files to the group's S3 bucket:

* ``group-logo.png``: logo to display at the top of the page
* ``group-overview.md``: a description of your group and the Nextstrain builds your group provides

Create a new file named ``group-overview.md`` that will contain information about your group.
At the top of this file, provide a title for the page, a list of people who maintain the data, a website, and/or whether to show datasets and narratives from your group.
This information is technically known as the `YAML front matter <https://jekyllrb.com/docs/front-matter/>`_ for the file.

.. code-block:: yaml

   ---
   title: "Your Department of Health and Human Services"
   byline: "Your Name Here"
   website: https://
   showDatasets: true
   showNarratives: true
   ---

   A description of your organization goes here.

All fields are optional and either have generic defaults (like the title) or are omitted from the page by default (like the byline and website link).
Dataset and narrative listings are both shown (i.e. ``true``) by default if not specified otherwise in this file with a value of ``false``.

After the front matter (in the lines following the last ``---`` characters), write a description of your organization to provide context for users who can access your groups page.
Use `Markdown syntax <https://www.markdownguide.org/basic-syntax/>`_ to format the contents of your group description with headers, lists, links, etc.
This content will appear between the title/byline/website heading and the list of available datasets on the group's page.

Upload your logo and description to your group’s S3 bucket with :doc:`the nextstrain remote upload command <cli:commands/remote/upload>`.

.. code-block:: bash

   nextstrain remote upload s3://nextstrain-<group>/ \
     group-logo.png group-overview.md

To update your logo, description, or any other data in your group’s S3 bucket, run the ``nextstrain remote upload`` command again and the uploaded data will replace the previous contents in the bucket.

Removing
========

To remove the customizations, delete one or both of the files.

.. code-block:: bash

   nextstrain remote delete s3://nextstrain-<group>/group-logo.png
   nextstrain remote delete s3://nextstrain-<group>/group-overview.md
