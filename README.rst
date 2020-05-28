.. image:: https://github.com/ayushpallav/anthill/blob/master/docs/images/anthill-small.png

=======
Anthill
=======
An intelligent general purpose automation system.

|pypi| |build-status| |readthedocs|

:Version: 1.0.3
:Download: https://pypi.org/project/anthill/
:Documentation: https://anthill-python.readthedocs.io/en/latest/

.. |pypi| image:: https://img.shields.io/pypi/v/anthill.svg
        :target: https://pypi.python.org/pypi/anthill

.. |build-status| image:: https://img.shields.io/travis/ayushpallav/anthill.svg
        :target: https://travis-ci.com/ayushpallav/anthill
.. |readthedocs| image:: https://readthedocs.org/projects/anthill-python/badge/?version=latest
        :target: https://anthill-python.readthedocs.io/en/latest/
        :alt: Documentation Status


* Free software: MIT license


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

To install from ``git``:

::

    $ git clone https://github.com/ayushpallav/anthill.git
    $ cd anthill
    $ python setup.py install

Usage
-----

To build and run Anthill:

::

	anthill build /path/to/nest.yml -r

Sample nest.yml
---------------

::

	node:
	  - rule: "rule_1.py"
	action_1:
	  - rule: "rule_2.py"
	  - depends_on:
	    - node
	action_2:
	  - rule: "rule_3.py"
	  - depends_on: 
	    - node
	    - 'action_3'
	action_3:
	  - rule: "rule_4.py"
	  - depends_on: 
	    - action_1
	action_4:
	  - rule: "rule_5.py"
	  - depends_on:
	    - action_2
	    - action_3
