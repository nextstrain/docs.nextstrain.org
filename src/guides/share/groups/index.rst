===========================
Share via Nextstrain Groups
===========================

.. toctree::
    :hidden:

    Customize your page <customize>

.. hint::
    This how-to guide assumes familiarity with the :doc:`Nextstrain Groups
    </learn/groups/index>` feature and the :doc:`Nextstrain dataset files
    </reference/data-formats>` produced by :doc:`running a pathogen workflow
    </tutorials/running-a-phylogenetic-workflow>`.  We recommend reading about those first
    if you're not familiar with them.

Log in with the Nextstrain CLI
==============================

Before you can upload data to your Nextstrain Group, you need to log into nextstrain.org with the Nextstrain CLI's :doc:`cli:commands/login` command so it knows how to access your group's data.

.. code-block:: bash

    nextstrain login

Confirm that you have access to your group by running :doc:`cli:commands/whoami`.

.. code-block:: bash

    nextstrain whoami

You should see your group name in the output.

You can also try listing your group's datasets and narratives with :doc:`cli:commands/remote/list`.
Replace ``${GROUPNAME}`` below with your group name.

.. code-block:: bash

   nextstrain remote list nextstrain.org/groups/${GROUPNAME}

This will likely return nothing for now since groups start without any datasets or narratives.
However, the lack of an error is useful to see.


Upload a Nextstrain dataset
===========================

.. warning::
   Do not upload any files containing personally identifiable information (PII).
   This restriction applies for public and private groups.

Upload one or more Nextstrain datasets for your group using the :doc:`cli:commands/remote/upload` command.
An example using a dataset produced by our :doc:`ncov workflow <ncov:index>`.
The pattern of your dataset and sidecar filenames and desired display URL to upload may be different.

.. code-block:: bash

   nextstrain remote upload \
     nextstrain.org/groups/${GROUPNAME}/ncov/${YOUR_BUILD_NAME} \
       auspice/ncov_${YOUR_BUILD_NAME}.json \
       auspice/ncov_${YOUR_BUILD_NAME}_tip-frequencies.json \
       auspice/ncov_${YOUR_BUILD_NAME}_root-sequence.json

After the upload completes, it'll appear in the group listing when you run:

.. code-block:: bash

   nextstrain remote list nextstrain.org/groups/${GROUPNAME}

You can also navigate to your groups page on the web to see the dataset listed there.

If you have multiple datasets to upload, you can do so with one command if their filenames match the URLs you want.

.. code-block:: bash

   nextstrain remote upload nextstrain.org/groups/${GROUPNAME} auspice/*.json

Remove a dataset
================

Use the :doc:`cli:commands/remote/delete` command to remove a dataset or narrative you've uploaded.

.. code-block:: bash

   nextstrain remote delete nextstrain.org/groups/${GROUPNAME}/ncov/${YOUR_BUILD_NAME}

Example
=======

Below is an example of what the steps above look like for a user ``trs`` and group ``test``:

.. code-block:: console

    $ nextstrain login
    Logging into Nextstrain.org…

    Username: trs
    Password:

    Credentials saved to /home/tom/.nextstrain/secrets.

    Logged into nextstrain.org as trs.
    Log out with `nextstrain logout`.

    $ nextstrain whoami
    username: trs
    email: tsibley@…
    groups:
      - test/editors

    $ nextstrain remote list nextstrain.org/groups/test

    $ nextstrain remote upload \
        nextstrain.org/groups/test/ncov/example \
          auspice/ncov_example.json \
          auspice/ncov_example_tip-frequencies.json \
          auspice/ncov_example_root-sequence.json
    Uploading auspice/ncov_example.json as https://nextstrain.org/groups/test/ncov/example
    Uploading auspice/ncov_example_root-sequence.json as https://nextstrain.org/groups/test/ncov/example (root-sequence)
    Uploading auspice/ncov_example_tip-frequencies.json as https://nextstrain.org/groups/test/ncov/example (tip-frequencies)

    $ nextstrain remote list nextstrain.org/groups/test
    https://nextstrain.org/groups/test/ncov/example

    $ nextstrain remote delete nextstrain.org/groups/test/ncov/example
    Deleting nextstrain.org/groups/test/ncov/example

You'll of course have to login as yourself, and be sure to replace ``test`` with your group's name when you try it!


Learn more
==========

Learn more about the above commands and parameters in the following reference material:

* :doc:`cli:commands/remote/index`
* :doc:`cli:commands/remote/list`
* :doc:`cli:commands/remote/upload`
* :doc:`cli:commands/remote/download`
* :doc:`cli:commands/remote/delete`
* :doc:`cli:remotes/nextstrain.org`
