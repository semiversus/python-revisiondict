===================
Python RevisionDict
===================

.. image:: https://img.shields.io/pypi/v/revisiondict.svg
        :target: https://pypi.python.org/pypi/revisiondict

.. image:: https://img.shields.io/travis/semiversus/python-revisiondict.svg
        :target: https://travis-ci.org/semiversus/python-revisiondict

.. image:: https://codecov.io/gh/semiversus/python-revisiondict/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/semiversus/python-revisiondict
        
.. image:: https://img.shields.io/github/license/semiversus/python-revisiondict.svg
        :target: https://en.wikipedia.org/wiki/MIT_License
        
RevisionDict works like an ordinary dictionary with additional revision keeping of changes. It remembers the order that
keys were *updated* (in contrast to the ``OrderedDict`` which is remembering the order that keys are *inserted*).

Additional functionality compared to ``dict()``:

* ``.revision`` - returning the actual revision as integer (starting with 0)
* ``.base_revision`` - revision before oldest item changed (or 0 on empty dict)
* ``.key_to_revision(key)`` - return the revision when the given key was changed
* ``.checkout(start=0)`` - return a dict with changes since ``start``

Install
-------

.. code-block:: python

    pip install revisiondict
    
Example
-------

.. code::python

>>> d=RevisionDict()
>>> d.revision                    # get revision (is 0 at init)
0
>>> d.base_revision               # get revision before oldest change
0

Adding new items:

.. code::python

>>> d['a']=0; d['b']=1; d['c']=2  # make three updates
>>> d.revision                    # showing 3 changes
3
>>> d.base_revision               # get revision before oldest change
0

Inspecting content of RevisionDict:

.. code::python

>>> d.checkout()=={'a': 0, 'b': 1, 'c': 2} # get a dictionary with all changes
True
>>> d.checkout(2)                 # get all changes starting with rev. 2
{'c': 2}
>>> d.checkout(3)                 # all changes starting with actual revision
{}
>>> d.key_to_revision('b')        # revision where 'b' was changed last time
2
>>> d
RevisionDict([_Item(key='a', value=0, revision=1), _Item(key='b', value=1, revision=2), _Item(key='c', value=2, revision=3)])

Update items:

.. code::python

>>> d['a']=3                      # update value of 'b' (was 2 before)
>>> d.revision
4
>>> d.base_revision
1
>>> d.key_to_revision('a')
4
>>> d.checkout(3)                 # get all changes starting with rev. 3
{'a': 3}
>>> tuple(d.keys())               # iterate over keys (ordered by time of update)
('b', 'c', 'a')
