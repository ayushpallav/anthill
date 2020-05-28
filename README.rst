=======
Anthill
=======

|pypi| |build-status| |readthedocs|

:Version: 1.3.0
:Download: https://pypi.org/project/anthill/

.. |pypi| image:: https://img.shields.io/pypi/v/anthill.svg
        :target: https://pypi.python.org/pypi/anthill

.. |build-status| image:: https://img.shields.io/travis/ayushpallav/anthill.svg
        :target: https://travis-ci.com/ayushpallav/anthill
.. |readthedocs| image:: https://readthedocs.org/projects/anthill-python/badge/?version=latest
        :target: https://anthill-python.readthedocs.io/en/latest/
        :alt: Documentation Status


An intelligent general purpose automation system.


* Free software: MIT license
* Documentation: https://anthill-python.readthedocs.io/en/latest/


What is a Nest?
----------------

A Nest is a blueprint to be used for building an Anthill. It is to be provided as a .yml configuration,
containing information about node and actions with their inter-dependencies.

What is an Anthill?
-------------------

An Anthill is the order of execution of actions, build upon the nest configuration.

Installation
------------

You can install Anthill either via the Python Package Index (PyPI)
or from source.

To install using ``pip``:

::


    $ pip install anthill

To install from ``source (git)``

::

    $ git clone https://github.com/ayushpallav/anthill.git
    $ cd anthill
    $ python setup.py install
