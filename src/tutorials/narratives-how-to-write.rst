===================
Writing a narrative
===================

The following will walk you through writing a Nextstrain narrative.
We'll start with a basic 2-slide narrative and then gradually add further slides with the intention
of describing the functionality of narratives. The aim is for you to feel comfortable with
the technical aspects of creating and troubleshooting narratives.


For an introduction to the concept of Narratives, please see :doc:`/guides/communicate/narratives-intro` or take a look at this example narrative,  `Twenty years of West Nile virus <https://nextstrain.org/narratives/twenty-years-of-WNV>`__.

This tutorial will rely on the new `Narratives Debugger <https://nextstrain.org/edit/narratives>`__ which allows you to drag & drop the Markdown files we'll introduce here and see an instant summary of the narrative.

.. contents:: Sections in this document
  :local:
  :depth: 2

.. note::

  This guide uses the narratives debugger on nextstrain.org; while you can also use this by running Auspice on your computer there are some differences - see :ref:`below for more details <auspice_vs_nextstrain>`.


Prerequisites
=============

To follow this tutorial, you will need:

* A (basic) understanding of writing Markdown `(here is good introduction) <https://learnxinyminutes.com/docs/markdown/>`__.
* Familiarity with the general concept of Nextstrain Narratives (see :doc:`/guides/communicate/narratives-intro` to get started).
* Ability to edit a Markdown file on your computer (in any text editor).
* The `Narratives Debugger <https://nextstrain.org/edit/narratives>`__ open in an internet browser.

The basics of how a narrative works
===================================

The content of a narrative is all within a single Markdown file, and this file contains nextstrain.org URLs from which the interactive visualisations are sourced.
We'll introduce the basic functionality via an example Markdown file below, which describes three slides:

1. The title slide (the section surrounded by ``---`` lines)
2. A slide showing the latest available monkeypox phylogeny
3. A slide looking back at the rise and fall of Influenza clades over the past 12 years

.. _example:

.. code-block:: markdown

  ---
  title: Introduction to narratives
  authors: Nextstrain
  authorLinks: "https://nextstrain.org"
  date: "2022-11-01"
  dataset: "https://nextstrain.org/monkeypox/hmpxv1?d=map&p=full&c=region"
  abstract: "
  3-slide narrative to introduce how to write narratives.
  This narrative is intended to be used as part out the
  [Writing a Narrative](https://docs.nextstrain.org/en/latest/tutorials/narratives-how-to-write.html)
  tutorial. 

  This opening slide is looking at monkeypox genomes focusing
  on the current outbreak. This view into the data is taken from
  the associated URL: https://nextstrain.org/monkeypox/hmpxv1?d=map&p=full&c=region
  "
  ---
  
  # [Monkeypox](https://nextstrain.org/monkeypox/hmpxv1?d=tree&p=full&c=region)

  We've now changed the view from the map to the phylogenic tree.
  This was achieved by changing the dataset URL to indicate that
  the display panel should change from the map to the tree.

  ```
  Title slide: monkeypox/hmpxv1?d=map
  This slide:  monkeypox/hmpxv1?d=tree
                                  ^^^^
  ```

  In practice, you don't need to remember the URL syntax, rather
  you can manipulate the visualization (on nextstrain.org) and then
  simply copy & paste the URL once you are happy with the current
  view into the data.


  P.S. The B.1 clade is the main outbreak clade & we can see a distinct
  comb-like appearance, with limited clustering of samples.
  This structure is typical of new, fast-spreading outbreaks.
  The tree is colored by region & we can see that the outbreak clade
  is dominated by samples from Europe and the Americas, whereas the
  basal (older) cases were typically from Africa.


  # [The rise and fall of Influenza clades](https://nextstrain.org/flu/seasonal/h3n2/ha/12y?d=tree,frequencies&p=full)

  We switch now to a completely different viral phylogeny - that of
  Influenza H3N2 over 12 years. This switch was made by defining a
  different dataset in the URL associated with this slide
  (https://nextstrain.org/flu/seasonal/h3n2/ha/12y?d=tree,frequencies&p=full).
  It is this URL which specifies that we should view both the tree & the
  frequencies panel 👉

  P.S. This phylogenetic structure is very different, more latter-like than
  comb like, a phenomena which is linked to antigenic evolution
  ([Bedford, Rambaut & Pascual, 2012](https://bmcbiol.biomedcentral.com/articles/10.1186/1741-7007-10-38)).


You can see a copy of this Markdown file `on GitHub <https://github.com/nextstrain/narratives/blob/master/how-to-write_basics.md>`__, and you can see the resulting narrative displayed in Nextstrain at `nextstrain.org/narratives/how-to-write/basics <https://nextstrain.org/narratives/how-to-write/basics>`__.


This tutorial will make use of our narratives debugger, which is available at `nextstrain.org/edit/narratives <https://nextstrain.org/edit/narratives>`__.
To introduce this functionality, let's copy / download the above Markdown to a file on your computer (the filename doesn't matter, as long as it finishes with ``.md``).
We can then drag the Markdown file onto the Narrative Debugger page and you should see something like the top half of this figure:


.. image :: ../images/narratives_debugger_screenshot.jpg
   :alt: Screenshot of the example narrative loaded in the narratives debugger and a preview of the opening slide


We can see the titles of the three slides & their associated datasets (see the following section for details on how titles are defined), and hovering over these should show you the full appearance of the slide.
To the right of the titles are their associate datasets, each with a series of icons next to them representing the main + sidecar JSONs associated with this dataset.
The icons represent whether the dataset exists on nextstrain.org -- in this case, they are all green (success) or grey (not attempted).
When debugging a narrative it's easy to make syntax errors resulting in datasets which don't load -- you could try changing the URLs in the Markdown file and dragging the file back onto the debugger to see this.
Clicking on the title of a slide will jump into the narrative at that slide, or you can click the "View Narrative" button to start from the beginning.


.. note::

  The narrative file you drag onto the debugger remains within your browser and is not sent to the Nextstrain server.
  The datasets it specifies must be accessible through nextstrain.org and are fetched (downloaded) when you are testing a narrative; these can include private Nextstrain Groups assuming you are logged into nextstrain.org & can access those private datasets.



A typical writing process
=========================

Hopefully the above section gives you enough to get started writing your own narratives.
There are more technical details to follow, but if you want to get started we encourage trying it out!
There are plenty of ways to approach the task, but we find the following workflow tends to work well:


.. graphviz::
    :align: center

    strict digraph {
        node [
            fontname="Lato, 'Helvetica Neue', sans-serif"
        ]
        edge [
            fontname="Lato, 'Helvetica Neue', sans-serif"
        ]
        rankdir="LR";
        auspice [shape="tab" style="filled" fillcolor="#c7e9b4" label="nextstrain.org/...\nto choose desired \nview of data"]
        md [shape="note" style="filled" fillcolor="#41b6c4" label="Narrative file\nwe are writing\n(Markdown)"]
        debugger [shape="tab" style="filled" fontcolor="white" fillcolor="#225ea8" label="Narratives debugger\nto test narrative\nas we go"]
        
        auspice -> md [label="copy\nURL" fontcolor="#7fcdbb" fillcolor="#7fcdbb" color="#7fcdbb"]
        md -> auspice [label="repeat" fontcolor="#7fcdbb" fillcolor="#7fcdbb" color="#7fcdbb" splines=curved]
        md -> debugger [label="drag &\ndrop" fontcolor="#1d91c0" fillcolor="#1d91c0" color="#1d91c0"]
        debugger -> md [label="repeat" fontcolor="#1d91c0" fillcolor="#1d91c0" color="#1d91c0" splines=curved]
    }

In the future we plan to add more and more editing capability into the debugger, but for now any changes to the narrative must be made in the Markdown file itself.
When you are happy with the end result, :ref:`see below for how to publish it on nextstrain.org <sharing>`.



Understanding the structure of narrative slides
===================================================


Title slide (frontmatter)
-------------------------

The opening (title) slide is defined in the Markdown file by an opening `YAML <https://learnxinyminutes.com/docs/yaml/>`__ frontmatter block, which is the part between the two ``---`` lines in the above example.
This defines a number of key-value pairs which we transform into the slide you see, all of which are optional except ``title`` and ``dataset``.
The possible content which can be rendered is listed below, in the order they would appear on screen:

#. The main title is taken from the ``title`` key.
#. The authors are then listed; these can be provided via ``authors`` and ``authorsLinks`` which should either both be strings or both be arrays of the same length. The ``authorsLinks`` is optional but recommended!
#. Any translators are then listed, encoded in the same format as the authors but using keys ``translators`` and ``translatorLinks``.
#. The abstract, defined by ``abstract`` is a string which will be rendered as Markdown [#f1]_.
#. When the narrative was first created (``date``) and when it was most recently updated (``updated``) is then displayed.
#. Finally, any applicable license is shown, as defined by ``license`` and ``licenseLink``.
#. The ``dataset`` is required and defines the data view in the right hand side of screen (see :ref:`see below <linking-view-to-url>`).


Normal slides
-------------

The rest of the Markdown file defines one or more slides, where each slide is defined by a level 1 heading which is also a link to a dataset on nextstrain.org [#f2]_ and a section of Markdown which represents the slide's content:


.. code-block:: markdown

  # [slide title here](nextstrain.org dataset URL here, including (optional) query params)

  Markdown content of the slide

As a real example (taken from above), we have:

.. code-block:: markdown

  # [The rise and fall of Influenza clades](https://nextstrain.org/flu/seasonal/h3n2/ha/12y?d=tree,frequencies&p=full)

  We switch now to a completely different viral phylogeny - that of Influenza H3N2 over 12 years.


The dataset URL :ref:`is detailed below<linking-view-to-url>` and defines the view into the data shown to the right of the rendered Markdown content.

.. _linking-view-to-url:

Linking the view into the data to the URL
-----------------------------------------

At the heart of narratives is the ability for URLs on nextstrain.org to encode not only the dataset to display but also the view settings, such as the coloring used, via the `URL query <https://en.wikipedia.org/wiki/Query_string>`__.  
You can see this in action by changing the view settings of a dataset on nextstrain.org and observing the URL query changing.
The available query parameters are detailed in Auspice's :doc:`auspice:advanced-functionality/view-settings` docs, however in most cases it's easier to manipulate the visualisation in-browser and then copy the resulting URL into your narrative.

Using our example narrative introduced :ref:`above<example>` we can see that the three slides use the following dataset URLs:

#. https://nextstrain.org/monkeypox/hmpxv1?d=map&p=full&c=region
#. https://nextstrain.org/monkeypox/hmpxv1?d=tree&p=full&c=region
#. https://nextstrain.org/flu/seasonal/h3n2/ha/12y?d=tree,frequencies&p=full

The only difference between 1 & 2 is the change from ``d=map`` to ``d=tree`` and so when we change between these slides in the narrative we simply change the map for the tree panel (or vice versa). Slide 3 uses a different dataset, and specifies both the tree and frequency panels.




.. _sharing:

Sharing / publishing narratives
===============================

There are a number of ways you can share the narrative further, including public and private options.
Please see :doc:`/guides/share/index` for more details.

For a temporary, ad-hoc solution while writing narratives, you could share the Markdown file and then drag it onto the debugger each time!


Advanced functionality / FAQ
============================


Main Display Markdown
---------------------

It's possible to replace the right-hand side view into the data with a full page Markdown rendering, which is useful for adding a large image in a narrative etc. This is done via a specific code fence within the Markdown content of a slide:

.. code-block:: markdown

  # [slide title](dataset URL)

  Slide content rendered in the left-hand sidebar (as normal)

  ```auspiceMainDisplayMarkdown

  Markdown content rendered in the right-hand pane of the display, where the dataset would normally be.

  _Note that the dataset URL is still required, although unused._

  ```

Embedding images
----------------

Publicaly accessible images can be embedded using normal Markdown syntax, for example using `this SEM photo of Yersinia Pestis <https://commons.wikimedia.org/wiki/File:Yersinia_pestis.jpg>`__:

.. code-block:: markdown

  ### Here's a SEM photo of Y. pestis

  ![Y pestis SEM](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Yersinia_pestis.jpg/800px-Yersinia_pestis.jpg)


If the image is not publicly accessible via a URL, you can also embed it in the Markdown file itself using base64 encoding [#f3]_ (see `here <https://www.base64-image.de/>`__ for a drag-and-drop utility to convert images to base64):

.. code-block:: markdown

  ![alt text](data:image/png;base64,<image-in-base64-encoding>)

.. _auspice_vs_nextstrain:

Differences between localhost (Auspice) and nextstrain.org
----------------------------------------------------------

It's possible to run a local instance of Auspice (the phylogenetic visualisation app used in nextstrain.org) and view narratives locally, however there are some differences between this and nextstrain.org which are really easy to get tripped up on!
Specifically the hostname is *not* used [#f2]_ -- only the pathname is used, and the way the dataset pathname is interpreted is different: Auspice can only access datasets on your computer (in the directory you supply via ``--datasetDir``) whereas nextstrain.org accesses data from :doc:`a range of places </guides/share/index>`.

The following example of a narrative slide may make this difference clearer:

.. code-block:: markdown

  # [Which dataset is this?](https://nextstrain.org/community/inrb-drc/ebola-nord-kivu)

  The dataset displayed here differs if you run it on localhost (auspice)
  or through nextstrain.org.

  When viewed on nextstrain.org this dataset is sourced from
  [this GitHub repository](https://github.com/inrb-drc/ebola-nord-kivu)
  as it is using our
  [community sharing functionality](https://docs.nextstrain.org/en/latest/guides/share/community-builds.html).

  To work when running on auspice locally, we would need to have a dataset
  with the following filename: `community_inrb-drc_ebola-nord-kivu.json`.



This complexity encouraged us to build the interactive debugger we have used in this tutorial and we encourage to use that approach rather than developing your narratives using Auspice locally & then trying to share them through nextstrain.org!


Where can I find some example narratives to use as inspiration?
---------------------------------------------------------------

All of the narratives written by the core Nextstrain team are available in `this GitHub repo <https://github.com/nextstrain/narratives>`__.

Future directions
-----------------

The app used to test narratives is in its infancy.
We hope to incrementally add features such as Markdown editing, changing the dataset view settings, and the ability to publish the narrative to :doc:`Nextstrain Groups </learn/groups/index>`.
The eventual aim is to be able to write & publish an entire narrative from within the app, without needing to know any specifics of the Markdown language behind it.

Next steps
==========

The aim is to author your own narratives, so we suggest adapting the Markdown files introduced below to
form your own narrative once you've worked through the tutorial. For this you'll need:

* One or more datasets that you wish to visualise, and these should be accessible via `nextstrain.org <https://nextstrain.org>`__. See :doc:`/guides/share/index` for more information.
* An idea of what you wish to write for each slide (you can always start with a single slide and add more as you go).

Bugs? Improvements? Suggestions?
================================

The debugger (as of November 2022) is in a beta-release phase. Please get in touch if you have suggestions or find bugs!
You can submit an `issue on GitHub <https://github.com/nextstrain/nextstrain.org/>`__ or make a post on our `discussion forum <https://discussion.nextstrain.org/>`__.




--------------

.. rubric:: Footnotes

.. [#f1] The provided string is actually rendered as ``### <abstract>``, so the first line will appear as a h3 heading!
  Multiple line strings are possible in YAML and we suggest using these.

.. [#f2] In practice, the URL path component is what is used to access the dataset relative to the current hostname, however for historical reasons the protocol and hostname must be either ``http://localhost:4000`` or ``https://nextstrain.org``. 

.. [#f3] This isn't great from a file-size point of view, and the Markdown file isn't nice to look at itself, but it gets around the problem of where to store images by embedding them in the file itself.
