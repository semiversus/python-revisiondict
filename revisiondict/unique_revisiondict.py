from revisiondict import RevisionDict


class UniqueRevisionDict(RevisionDict):
    """ UniqueRevisionDict is a RevisionDict that does not increase the revision when a value is set to the
        same value as before.

        >>> d = UniqueRevisionDict()
        >>> d['a']=0; d['b']=1; d['c']=2  # make three updates
        >>> d.revision
        3
        >>> d.base_revision
        0
        >>> d['a']=0                      # update value of 'a' (was 0 before)
        >>> d.revision
        3
        >>> d['a']=3
        >>> d.revision
        4
    """
    
    def __setitem__(self, key, value):
        if key in self._key_to_index and value == self._items[self._key_to_index[key]].value:
            return
        RevisionDict.__setitem__(self, key, value)