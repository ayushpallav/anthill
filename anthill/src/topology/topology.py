import json
import logging

from .transform import TransformNest

log = logging.getLogger(__name__)


class Anthill:
    """
    Anthill is a topoLOGICAL order of ants.
    Ants are the basic block, consisting of singular functions
    These singular functions whene arranges in a logical order form an
    anthill.
    - Anthill:
    [
        {
            "label": "",
            "meta": {
                "rule": "",
                "depends_on": []
            }
        }
    ]
    """
    _nest = None
    anthill = []
    _anthill_inx = []
    action_map = None
    lookup_map = None
    adj_list = None

    def __init__(self, nest):
        self.nest = json.loads(nest)

    def assign_meta_variables(self, _nmt):
        self.action_map = _nmt.action_map
        self.lookup_map = _nmt.lookup_map
        self.adj_list = _nmt.adj_list

    def get_anthill_action(self, inx):
        """
        Get action agaist inx
        """
        label = self.action_map[inx]
        _meta = {}
        for item in self.nest[label]:
            _meta.update(**item)
        return dict(
            label=label,
            meta=_meta
        )

    def set_next_inx(self):
        """
        Set next action in topological order
        """
        for inx in self.lookup_map:
            if inx not in self._anthill_inx and self.lookup_map[inx]==0:
                self._anthill_inx.append(inx)
                return inx
        return -1

    def update_lookup_map(self, inx):
        """
        Updates incoming branch count from lookup map
        """
        _dependents = self.adj_list[inx]
        for it in _dependents:
            self.lookup_map[it] -= 1

    def _build(self):
        """
        Build anthill from _anthill_inx
        """
        self.anthill = [self.get_anthill_action(x) for x in self._anthill_inx]

    def build(self):
        self.assign_meta_variables(
            TransformNest(nest=self.nest).transform()
        )
        while True:
            inx  = self.set_next_inx()
            if inx==-1:
                break
            self.update_lookup_map(inx)
        self._build()
        return self.anthill
