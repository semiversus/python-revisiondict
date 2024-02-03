""" RevisionDict works like an ordinary dictionary with "
                "additional revision keeping of changes.
"""

__author__ = 'Günther Jena'
__email__ = 'guenther@jena.at'

try:
    from ._version import version as __version__  # type: ignore
except ImportError:
    __version__ = 'not available'

from .revisiondict import RevisionDict
from .unique_revisiondict import UniqueRevisionDict

__all__ = ['RevisionDict', 'UniqueRevisionDict']
