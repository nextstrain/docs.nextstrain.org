
======================================
Sharing Analyses through Nextstrain
======================================

.. toctree::
   :maxdepth: 2
   :titlesonly:
   :hidden:

   nextstrain-groups
   community-builds
   fetch-via-urls
   sars-cov-2
   Download data <download-data>


Our Philosophy: Facilitating Open-Science & Sharing of Results
==============================================================

From the beginning, Nextstrain has focused on open, real-time, pre-publication sharing of results.
Every situation is different and over time we've tried to develop a range of different approaches to take steps in this direction wherever possible.

Here is a summary of the different ways one can share data through `nextstrain.org`_ or using the tools which are behind Nextstrain:


================================== =========================== ============================ =================== ===========================
Name                               Data stored on…             Accessed via…                Visibility          Managed by…
================================== =========================== ============================ =================== ===========================
`Nextstrain-maintained pathogens`_ nextstrain.org              `nextstrain.org`_            Public              the Nextstrain team
`Nextstrain Community`_            Your own GitHub repo        nextstrain.org/community/... Public              You, via GitHub
`Nextstrain Groups`_               nextstrain.org              nextstrain.org/groups/...    Public or private   You, via the Nextstrain CLI
`Public URLs`_                     Anywhere HTTPS-accessible   nextstrain.org/fetch/...     Public              You, via your web host
`auspice.us`_                      Your computer               `auspice.us`_                Private             You, via your file manager
`Custom auspice servers`_          Wherever you choose         Your own server's URL        Your choice         You, however you choose
================================== =========================== ============================ =================== ===========================


We are always excited to help you contribute to Nextstrain, no matter what shape this takes.
Please `get in touch with us <mailto:hello@nextstrain.org>`__  with any specific questions and we'll be happy to help.


Centrally Maintained, Regularly Updated Datasets
------------------------------------------------

There are a number of datasets which are run by the Nextstrain team or close collaborators, for instance `SARS-CoV-2 <https://nextstrain.org/ncov/global>`__, `seasonal influenza <https://nextstrain.org/flu>`__, and `West Nile virus <https://nextstrain.org/WNV/NA>`__.
Each individual dataset contains links to the scientists who maintain it.

We're exited to collaborate with more research groups and expand these datasets -- please `get in touch with us <mailto:hello@nextstrain.org>`__ if this is something you'd like to be involved in.


Community Maintained Datasets
-----------------------------

To make supporting this philosophy as easy as possible, we have created a "community builds" functionality, whereby GitHub is used to store the results of your analyses and the results are available for everyone via nextstrain.org.
This is behind the `community builds <https://nextstrain.org/#community>`__ which you can see on the main page.

See :doc:`community-builds` for more information, including a step-by-step guide on how you can get your datasets up as a community build.

Nextstrain Groups
-----------------

Groups are an initiative to allow research labs, public health entities and others to manage their own datasets and narratives and share them through nextstrain.org.
Groups can either be private or public in order to allow data sharing to the correct audience -- you can see an example of a public group `here <https://nextstrain.org/groups/blab>`__.
Private groups will only be visible to people who have a login to nextstrain.org and the permissions to see datasets in the group.

Nextstrain Groups are more scalable than community managed datasets, especially if you have many large datasets, and we're excited with the future possibilities that this opens up.

See :doc:`nextstrain-groups` for more information.

auspice.us
-------------

`auspice.us`_ allows you to simply drag and drop files onto the browser and have a fully-functioning interactive visualisation similar to those you've seen on nextstrain.org.
Since the data never leaves your computer (it's all done client-side) this can be a useful way to visualise sensitive data without needing to run auspice locally or manage your own server.

Please visit `auspice.us`_ to see the full list of currently supported file types.

Custom Auspice Servers
----------------------

Auspice can be run on your own server, including customizations to the appearance and functionality.
This may be appropriate when you want or need full control over how the website is deployed and where the data is stored.
Please see the :doc:`the auspice docs <auspice:index>` for more information on how to set this up.


.. _Nextstrain-maintained pathogens: https://nextstrain.org/pathogens
.. _Nextstrain Community: community-builds
.. _Nextstrain Groups: nextstrain-groups
.. _Custom auspice servers: auspice:server/index
.. _Public URLs: fetch-via-urls
.. _auspice.us: https://auspice.us
.. _nextstrain.org: http://nextstrain.org
