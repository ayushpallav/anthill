import logging

from .transform import TransformNest

log = logging.getLogger(__name__)


class Anthill:
    """
    Anthill is a topoLOGICAL order of ants.
    Ants are the basic block, consisting of singular functions
    These singular functions whene arranges in a logical order form an
    anthill.
    """
    _nest = None

    def __init__(self, nest):
        self.nest = nest

    def transform(self):
        self._nest = TransformNest(nest=self.nest).transform()

    def build(self):
        self.transform()
