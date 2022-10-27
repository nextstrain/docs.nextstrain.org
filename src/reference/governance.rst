.. This document was initially drafted in Google Docs¹ and discussed during the
   27 October 2022 general meeting².
   
   ¹ https://docs.google.com/document/d/1qWi0S6B1SPesYvC7lYvjN6j8pevubL1qvtYp3pRrGLs/edit
   ² https://docs.google.com/document/d/1SFUa6w1hdwx9ooYAGaTfq70NrdWYmlQDm_cNVce5FH8/edit

==========
Governance
==========

The governance of the Nextstrain project is relatively informal.
The structure and processes that do exist are briefly described below in the interests of transparency.

Organizational structure
========================

.. Using the glossary directive here lets us link to these terms in other
   documents (see mostly gratutitous examples of doing so below).  Being able to
   do so seems useful, for example, in other places we might want to refer to the
   "core team" (e.g. often as the "Nextstrain team").

.. glossary::

    Project Leads
        The Project Leads are the two co-creators of Nextstrain:

          - `Trevor Bedford <https://bedford.io/team/trevor-bedford/>`__
          - `Richard Neher <https://neherlab.org/richard-neher.html>`__

        The Project Leads have the authority to make all final decisions for the project.
        In practice, the Project Leads usually choose to defer that authority to the consensus of the :term:`Core Team`.

    Core Team
        Active and substantial contributors to Nextstrain including :term:`Project Leads` who have enough context on the project and its components to contribute to decision-making.

    Community Contributors
        Occasional contributors including those from `Bedford Lab <https://bedford.io>`__, `Neher Lab <https://neherlab.org>`__, alumni, or other external groups.
        Influences decision-making but does not directly participate in it.


Decision-making
===============

Nextstrain's decision-making process seeks to balance broad participation of stakeholders with agility.
The following list of decision-making approaches is in order from most to least preferred.

Seek consensus from the Core Team.
   - Alert the team about major changes (e.g., via Slack) or to request feedback (e.g., via Slack or GitHub reviewer requests).
   - Allow enough time for team members to review and register feedback before finalizing a decision.
   - Summarize the consensus decision publicly (e.g., on a GitHub PR or issue).
   - Alert the team that a consensus has been reached on major changes (e.g., via Slack or GitHub).
   - For critical, urgent, or stalled decisions, arrange a synchronous meeting to review available options and attempt to reach a decision during the meeting (e.g., biweekly Nextstrain meeting, biweekly issue triage meeting, or a special topic meeting).
   - Minimally, seek consensus with at least one other Core Team member who is familiar with the context.

Hold an informal vote to gauge opinion on difficult or subjective decisions (e.g., naming).
   - Hold votes publicly (e.g., vote with thumbs up or down on a GitHub comment).
   - Allow enough time for team members to vote.
   - Summarize the vote and ask for concerns (e.g., vetoes).

Bypass consensus with a decision by a single Core Team member who has expertise in the matter at hand.
   - Use for uncontroversial decisions or decisions on matters where the Core Team lacks expertise or strong opinions.
   - Provide the Core Team an opportunity to register their lack of a strong opinion. Err on the side of "over-communicating" to the team.
   - Document the final decision publicly.

Request tie-breaking or overruling vote from Project Leads.
   - Use as a last resort when consensus cannot be reached for critical and/or time-sensitive decisions.


Code review
===========

Our `practice of code review <https://wiki.nextstrain.org/t/code+review>`__ (internal doc) often informally trigger a request for a decision from the Core Team.
The informal nature of this process can result in a lack of feedback from the Core Team causing the corresponding Pull Request (PR) to stall on review without conclusion [#warnock]_.
The stalling means the people involved in the PR (author and reviewers) have spent time on something that's now in an ambiguous state of "reviewed, needs more work" and is effectively blocked indefinitely.
Both PR authors and other team members can benefit from a more concrete decision of:

  1. **Yes**, this should be pushed to finish soon while it's fresh in our minds.
  2. **No**, let's close this and label it as "shelved", reserving the option to re-open later.

We use the decision-making process described above to break a deadlock or move forward on a stalled PR.

Related documentation
=====================

This governance document is inspired by the following related documents.

  - `Producing Open Source Software: Social and Political Infrastructure <https://producingoss.com/en/producingoss.html#social-infrastructure>`_
  - `Matplotlib Main Governance Document <https://matplotlib.org/governance/governance.html>`_
  - `NumPy project governance and decision-making <https://numpy.org/doc/stable/dev/governance/governance.html>`_

.. rubric:: Footnotes

.. [#warnock] `Similar to Warnock's dilemma <https://en.wikipedia.org/wiki/Warnock%27s_dilemma>`_.
