========================================================================
Migrate data management for a Nextstrain Group from S3 to nextstrain.org
========================================================================

.. hint::
    This guide only applies to :doc:`Nextstrain Groups </learn/groups/index>`
    created **before March 2022**.

What
====

We've improved the way to manage datasets and narratives in :doc:`Nextstrain
Groups </learn/groups/index>`.  Now the Nextstrain CLI will directly interact
with nextstrain.org instead of interacting with a group-associated AWS S3
bucket (e.g. ``s3://nextstrain-${GROUPNAME}/``).

For comparison, here's an example of the old way vs. the new way to upload a
dataset to a Nextstrain Group:

.. code-block:: bash
    :emphasize-lines: 3,10

    # Old way
    nextstrain remote upload \
      s3://nextstrain-${GROUPNAME}/ \
        auspice/${YOUR_BUILD_NAME}.json \
        auspice/${YOUR_BUILD_NAME}_tip-frequencies.json \
        auspice/${YOUR_BUILD_NAME}_root-sequence.json

    # New way
    nextstrain remote upload \
      nextstrain.org/groups/${GROUPNAME} \
        auspice/${YOUR_BUILD_NAME}.json \
        auspice/${YOUR_BUILD_NAME}_tip-frequencies.json \
        auspice/${YOUR_BUILD_NAME}_root-sequence.json

Each group must undergo a short migration (performed by us) in order to use the
new way.  Groups which haven't been migrated will continue to use the old way.

With the new way, group data is still stored in S3 with access controlled by
Nextstrain, but now you no longer need to setup or pass around AWS credentials
provided to you by Nextstrain.  Instead, you will :doc:`login
<cli:commands/login>` using the same nextstrain.org username and password you
use to login to the website.  Each CLI login session is valid for at most 30
days, after which you'll need to login again.  Commands requiring login will
prompt you to do so when necessary.


Why
===

This change simplifies the management of Nextstrain Groups for both users and
ourselves, primarily by removing the need to setup and keep track of a separate
set of AWS credentials for each group.  It also makes it easier for us to
provision new groups, which is an important step in making Nextstrain Groups
more widely available.

The new :ref:`membership roles <groups-roles>` are made possible by the change,
including the possibility of finer-grained roles/permissions as necessary in
the future.


Actions requested
=================

Each group is migrated independently of any others.  To make your group's
migration as smooth as possible, we're requesting some help from you.

Before migration
----------------

1. **Pick a date and/or time of day you'd like the migration to happen.**

   During the brief migration period (less than an hour), you won't be able to
   manage your group's data.  However, you'll be able to view the datasets and
   narratives in your group on nextstrain.org the whole time, without any
   downtime.

   If you have no preference, you may leave it up to us to pick a date and
   time.

2. **Decide on roles for existing group members**.

   Groups now support three :ref:`membership roles <groups-roles>` (viewers,
   editors, and owners) which determine who can manage data.

   By default, all existing members will be **viewers** unless you tell us
   otherwise.

3. **Request that we migrate your group** by `emailing us
   <mailto:hello@nextstrain.org>`__.

   Include your preferred date and/or time of day and the list of roles for
   existing members.  We'll confirm the date and time of your migration in
   advance of performing it.

   .. note::
       If you frequently update your group's :ref:`overview or logo files
       <group-customization>`, please `email us`_ to let us know and wait to
       migrate until we've added support for updating these files yourself when
       not using a separate S3 bucket.

4. **Upgrade the version of the Nextstrain CLI you're using to at least 5.0.0.**

   It's best to do this in advance of the migration so you're set to keep using
   your group afterwards without having to upgrade later, but you may choose to
   wait.

   Check the version you have by running:

   .. code-block:: console

        $ nextstrain version
        nextstrain.cli 5.0.0

   If you see a version older than 5.0.0, please :doc:`upgrade your copy of the
   Nextstrain CLI <cli:upgrading>`.


After migration
---------------

We'll email you when your group's migration is complete.  From that point
forward, everyone managing your group's datasets and narratives will need to
use :doc:`"nextstrain remote" commands <cli:commands/remote/index>` which
reference your group's nextstrain.org URL instead of your previous S3 bucket
URL.  You will no longer have access to your previous S3 bucket, and after a
grace period of at least 30 days, it will be completely deleted.

It's a good idea to give these new commands a try shortly after the migration
to make sure everything works as expected for you.  For example, you might try
logging in and listing your group's datasets.  Here's what that looks like for
the user ``trs`` and the group ``blab``:

.. code-block:: console

    $ nextstrain login
    Logging into Nextstrain.org…

    Username: trs
    Password:

    Credentials saved to /home/tom/.nextstrain/secrets.

    Logged into nextstrain.org as trs.
    Log out with `nextstrain logout`.

    $ nextstrain remote list groups/blab
    https://nextstrain.org/groups/blab/Pf/K13
    https://nextstrain.org/groups/blab/Pf/chr13
    https://nextstrain.org/groups/blab/beta-cov
    https://nextstrain.org/groups/blab/ncov/19B
    …

You'll of course have to login as yourself, and be sure to replace ``blab``
with your group's name when you try it!

If you need to make changes to the roles of any group members or update your
group's :ref:`overview or logo file <group-customization>`, `email us`_ and
we'll take care of it.  In the future, group owners will be able to make these
changes themselves.

.. _email us: mailto:hello@nextstrain.org


Timeline
========

:March 2022: New groups created after this point manage their data through
             nextstrain.org instead of S3.

:early November: `Notification`_ sent to groups created prior to March.

:November onwards: Groups start migrating one-by-one in coordination with group owners.

:end of February 2023: Nextstrain team's desired deadline for migrating all groups.


Notification
============

In November 2022, we emailed the contacts for all groups created before March 2022
to inform them of these changes.  A copy of the email is below.

    **Subject:** Action requested: Improvements to how you manage your
    Nextstrain Group

    Hello!

    It's the Nextstrain team.  We're writing to let you know about improvements
    we've made to how you manage your data in Nextstrain Groups.  We've put
    together :doc:`a documentation page <migrate-from-s3>` with information
    about the changes, including the actions requested of you. **Please review
    the details there and reply to this email with the information requested.**

    You're receiving this email because you're a contact for one or more
    Nextstrain Groups:

      - https://nextstrain.org/groups/${*GROUPNAME*}

    Thank you for being an early adopter of Nextstrain Groups!  We're excited
    to keep improving the functionality of Groups.  If you have any feedback,
    please don't hesitate to `email us`_ or post to `discussions.nextstrain.org
    <https://discussions.nextstrain.org>`__.

    —the Nextstrain team
