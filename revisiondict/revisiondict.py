# -*- coding: utf-8 -*-

"""
RevisionDict works like an ordinary dictionary with additional revision keeping
of changes. It remembers the order when keys were *updated* (in contrast to the
``OrderedDict`` which is remembering the order when keys are *inserted*).

Additional functionality compared to ``dict()``:

* ``.revision`` - returning the actual revision as integer (starting with 0)
* ``.base_revision`` - revision before oldest item changed (or 0 on empty dict)
* ``.key_to_revision(key)`` - return revision when the given key was changed
* ``.checkout(start=0)`` - return a dict with changes since ``start``

>>> d=RevisionDict()
>>> d.revision                    # get revision (is 0 at init)
0
>>> d.base_revision               # get revision before oldest change
0

Adding new items:
>>> d['a']=0; d['b']=1; d['c']=2  # make three updates
>>> d.revision                    # get actual revision
3
>>> d.base_revision               # get revision before oldest change
0

Inspecting content of RevisionDict:
>>> d.checkout()=={'a': 0, 'b': 1, 'c': 2} # get a dictionary with all changes
True
>>> d.checkout(2)                 # get all changes starting with rev. 2
{'c': 2}
>>> d.checkout(d.revision)        # all changes starting with actual revision
{}
>>> d.key_to_revision('b')        # revision where 'b' was changed last time
2
>>> d
RevisionDict([_Item(key='a', value=0, revision=1), \
_Item(key='b', value=1, revision=2), \
_Item(key='c', value=2, revision=3)])


Update items:
>>> d['a']=3                      # update value of 'a' (was 0 before)
>>> d.revision
4
>>> d.base_revision
1
>>> d.key_to_revision('a')
4
>>> d.checkout(3)                 # get all changes starting with rev. 3
{'a': 3}
>>> tuple(d.keys())               # iterate over keys ordered by time of update
('b', 'c', 'a')
"""

import collections
import bisect


class _Item(collections.namedtuple('_Item', 'key value revision')):
    """ _Item representing a key:value pair with information about the revision
    this update was done.
    """

    def __lt__(self, other):
        """__lt__ method is used for bisect"""
        return self.revision < other.revision


class RevisionDict(collections.MutableMapping):
    def __init__(self, *args, **kwargs):
        self._items = list()  # keep _Item objs, guaranteed sorted by revision
        self._key_to_index = dict()  # dict indexing position of key in _items
        self._actual_revision = 0  # number of actual revision
        self.update(*args, **kwargs)

    def __setitem__(self, key, value):
        """ set value for given key and update the actual revision """
        self._actual_revision += 1
        if key in self._key_to_index:
            # if this key already available remove entry from self._items
            del self[key]
        self._key_to_index[key] = len(self._items)  # index the end of _items
        self._items.append(_Item(key, value, self._actual_revision))

    def __getitem__(self, key):
        """ return value to the given key """
        return self._items[self._key_to_index[key]].value

    def __delitem__(self, key):
        """ remove key from this collection """
        index = self._key_to_index.pop(key)  # pop this key and get index
        self._items.pop(index)  # remove that item entry
        self._key_to_index.update(  # update indicies for keys
            ((k, i - 1) for (k, i) in self._key_to_index.items() if i > index))

    def __iter__(self):
        """ returns a iterator over the keys sorted by revision """
        return iter(sorted(self._key_to_index, key=self._key_to_index.get))

    def __len__(self):
        """ return number of items """
        return len(self._items)

    @classmethod
    def fromkeys(cls, keys, value=None):
        """ create a new RevisionDict with keys from seq and given value """
        self = cls()
        for key in keys:
            self[key] = value
        return self

    def copy(self):
        """ returns a shallow copy of RevisionDict """
        d = RevisionDict()
        d._items = self._items[:]  # make a shallow copy of _items
        d._key_to_index = self._key_to_index.copy()
        d._actual_revision = self._actual_revision
        return d

    def has_key(self, key):
        """ test for presence of key. """
        # this method is deprecated and only for python2 compatability
        return key in self

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self._items)

    def key_to_revision(self, key):
        """ get revision when this key was updated last time """
        return self._items[self._key_to_index[key]].revision

    def checkout(self, start=None):
        """ get a dict() with all changes from revision `start` on """
        if start is not None:
            start_index = bisect.bisect(self._items, _Item(None, None, start))
        else:
            start_index = None
        return dict(((i.key, i.value) for i in self._items[start_index:]))

    @property
    def revision(self):
        """ get latest revision """
        return self._actual_revision

    @property
    def base_revision(self):
        """ revision before oldest change (or 0 on empty dict)"""
        return min((item.revision for item in self._items)) - 1 if \
            self._items else 0
