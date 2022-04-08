=================
Nextstrain Groups
=================

Nextstrain Groups is a feature that allows research labs, public health
entities, and other organizations to share their Nextstrain datasets and
narratives directly on `nextstrain.org <https://nextstrain.org>`_ within the
context of a named "group".  Groups can be shared :ref:`publicly or privately
<public-vs-private-groups>`.  See our summary of :doc:`ways to share your data
</guides/share/index>` for comparison of Nextstrain Groups with other sharing
methods.

.. note::
   Nextstrain Groups is still in the early stages and each group requires setup
   by the Nextstrain team.  Please `email us <mailto:hello@nextstrain.org>`__
   and we'd be happy to set up a group for you.

Pages
=====

Each group gets its own splash page at a base URL like:

    nextstrain.org/groups/*NAME*

The splash page consists of a group title, logo, and overview (all
:doc:`customizable </guides/share/groups/customize>`) plus listings of the
datasets and narratives in the group.  All datasets and narratives uploaded to
a group are viewable on their own pages at URLs of your choosing under the
group's base URL.

See `nextstrain.org/groups/blab <https://nextstrain.org/groups/blab>`__ and
`nextstrain.org/groups/neherlab <https://nextstrain.org/groups/neherlab>`__ for
examples of group splash pages.


Names
=====

The names of Nextstrain Groups are kind of like usernames: the ideal name is
short and simple but still clearly identifies your organization.  Group names
appear in the URL of your analyses and other places on nextstrain.org, such as
`listings of public datasets <https://nextstrain.org/groups>`__.  If you have a
pair of groups, one :term:`public` and one :term:`private`, we recommend naming
the private group using the name of the public group suffixed with "-private"
to clearly distinguish it.

Currently group names are required to be between 3–50 characters and consist of
only letters (a–z, A–Z), numbers (0–9), and hyphens (-).

If your organization has a long title or name, you can :ref:`customize your
group's splash page <group-customization>` to display the full name even if the
name of the group is a shorter abbreviation.


.. _public-vs-private-groups:

Public vs. private
==================

Groups may be designated **public** or **private**.  This visibility
designation applies to the entire group and its data.  A single organization
may manage more than one group to share both publicly and privately.

.. glossary::

    Public
        Visible to the general public (i.e. everyone).  No login is required to
        see the group page or view the datasets and narratives in the group.
        Public groups are listed at `nextstrain.org/groups
        <https://nextstrain.org/groups>`__.

    Private
        Visible only to the members of the group.  A nextstrain.org login is
        required to see the group page and view the datasets and narratives in
        the group.  While Nextstrain prevents unauthorized access to private
        groups, it does not try to hide their existence.

.. note::
    Future changes may allow for mixing private datasets or narratives within a
    public group and vice versa.  If this would be useful to you, please `email
    us`__ to let us know your interest.

    __ mailto:hello@nextstrain.org?subject=Interest%20in%20mixed%20public/private%20Groups


Members
=======

Anyone in your organization, on your team, or who you collaborate with can be
added as members of your group in order to share and collaborate with them.
Each person needs their own nextstrain.org username before being added as a
group member.

.. _groups-roles:

Roles
=====

Members of a group can belong to three roles.  A user's membership role
determines the permissions they have within the group.

.. glossary::

    Viewers
        Viewers have read-only access to the group.

        For :term:`private` groups, this role lets the user see the datasets
        and narratives within the group.  For :term:`public` groups, this role
        currently grants no additional access beyond that of non-members (e.g.
        the general public).

        In the future, this role is likely to also allow viewing of the group's
        members, their roles, and other information about the group itself that
        isn't public (even for public groups).

    Editors
        Editors have read-write access to the group.

        This includes the same permissions as :term:`viewers` plus the ability
        to upload, download, and delete datasets and narratives.

    Owners
        Owners have full control over the group.

        This includes the same permissions as :term:`editors` plus the ability
        to manage the group's description and logo [#owners1]_, invite and
        remove group members, change the roles of group members, and even
        delete the group entirely [#owners2]_.


.. [#owners1] Self-service for groups using their own S3 buckets; currently
              requires contacting the Nextstrain team for groups which have
              :doc:`migrated from S3 </guides/share/groups/migrate-from-s3>`.

.. [#owners2] Currently requires contacting the Nextstrain team.
