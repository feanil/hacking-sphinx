.. Test Sphinx Extension documentation master file, created by
   sphinx-quickstart on Fri Jan 28 15:06:11 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Test Sphinx Extension's documentation!
=================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Smart Replacement Testing
=========================

.. smart_replace::
   :source: https://gist.githubusercontent.com/feanil/c643ed5d6ecbbf6b91629670beed16e2/raw/21a34340ea16549470a1d389d5538d0a4c656b0c/test.rst


   - start_after: "specific to "
     end_before: " you should know"
     content: >
       edX.org

   - start_after: "It's "
     end_before: "."
     content: >
       something else

..
   .. note:: Testing

      This is only a test.


..
  .. note::
     .. note:: This is a note admonition.
        This is the second line of the first paragraph.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

