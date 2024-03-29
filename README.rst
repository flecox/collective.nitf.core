===============
collective.nitf
===============

.. contents:: Table of Contents

Overview
--------

News articles in Plone are instances of the 'News Item' content type: they can
contain a title, a description, a body text, an image and some basic metadata.
If you publish a couple of items from time to time, this is fine.

But suppose you have to publish dozens of items everyday... How do you tell
your readers who they are about? What do they cover? Where do they took place?
And, more important, how do you classify them? How do you organize them? How
do you tell your readers which ones are newsworthy?

To solve these, and other issues, the IPTC_ developed XML standards to define
the content and structure of news articles. NITF_, NewsML_ and NewsCodes_ are
among these standards and they support the classification, identification and
description of a huge number of news articles characteristics.

NITF is intended to structure independent news articles and this package aims
to implement a content type inspired by the specification.

Requirements
------------

* Plone >= 4.1
* Dexterity_ >= 1.2.1

Usage
-----
TBD

Helper views
^^^^^^^^^^^^

All news articles provide @@nitf and @@newsml views that are available
although are not registered.

Validating
^^^^^^^^^^

You can validate the output of the @@nitf and @@newsml views using services
like `XML validation`_.

You may use the `NITF Document Type Definition`_ version 3.5 and the `XHTML
Ruby Module`_ associated with it.

.. _Dexterity: http://pypi.python.org/pypi/plone.app.dexterity
.. _IPTC: http://www.iptc.org/
.. _NewsCodes: http://www.iptc.org/NewsCodes/
.. _NewsML: http://www.newsml.org/
.. _NITF: http://www.nitf.org/
.. _`NITF Document Type Definition`: http://www.iptc.org/std/NITF/3.5/specification/nitf-3-5.dtd
.. _`XHTML Ruby Module`: http://www.iptc.org/std/NITF/3.5/specification/xhtml-ruby-1.mod
.. _`XML validation`: http://www.xmlvalidation.com/

