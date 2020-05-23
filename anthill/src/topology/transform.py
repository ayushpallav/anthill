import json
import jsonschema
import logging
from collections import namedtuple

from .constants import Schema, Options

log = logging.getLogger(__name__)

# nmt = nest meta tuple
nmt = namedtuple('nmt', ['action_map', 'lookup_array', 'adj_list'])


class TransformNest:
    """
    This class processes the nest, that can be used
    to build an Anthill
    - I/P Nest:
    ...... {
    ......     "node": [{
    ......         "rule": "rule_1.json"
    ......     }],
    ......     "action_1": [{
    ......         "rule": "rule_2.json"
    ......     }, {
    ......         "depends_on": ["node"]
    ......     }]
    ...... }
    """
    action_map = None
    lookup_map = None
    adj_list = None

    def __init__(self, nest):
        self.nest = json.loads(nest)

    def is_valid(self):
        """
        Check Validity of pre-processed nest configuration
        """
        try:
            jsonschema.validate(
                instance=self.nest,
                schema=Schema.NEST_SCHEMA
            )
        except jsonschema.exceptions.ValidationError as err:
            log.error(f"Invalid nest ... \n {err.message}")
            return False
        return True

    def gen_action_map(self):
        """
        Generate mapping for
            <action_label, index>
        """
        return {
            key:value for key, value in enumerate(list(self.nest.keys()))
        }

    def _dependencies(self, action):
        """
        Returns the count of dependencies for the provided action
        """
        _count = [
            len(x[Options.DEPENDS_ON]) for x in action if Options.DEPENDS_ON in x.keys()
        ]
        if not _count:
            return 0
        return _count[0]

    def _get_action(self, inx):
        """
        Returns action corresponding to the index in
        action map
        """
        action_label = self.action_map.get(inx)
        return self.nest.get(action_label)

    def _get_inx(self, label):
        """
        Returns inx corresponding to action label
        from action_map
        """
        for _inx, _label in self.action_map.items():
            if _label == label:
                return _inx

    def gen_lookup_map(self):
        """
        Lookup map maps index to the total number
        of dependencies
        """
        lookup = {}
        for inx in self.action_map:
            _action = self._get_action(inx)
            lookup[inx] = self._dependencies(_action)
        return lookup

    def _dependents(self, inx):
        """
        Returns list of inx which are dependent on
        the provided inx
        """
        res = []
        action_label = self.action_map.get(inx)
        for _label in self.nest:
            _it = self.nest.get(_label)
            _it_dependencies = [
                x[Options.DEPENDS_ON] for x in _it if Options.DEPENDS_ON in x.keys()
            ]
            if _it_dependencies and action_label in _it_dependencies[0]:
                res.append(self._get_inx(_label))
        return res

    def gen_adj_list(self):
        """
        Generate adjancy list to be used to develop topology
        """
        adj_list = {}
        for inx in self.action_map:
            adj_list[inx] = self._dependents(inx)
        return adj_list

    def generate(self):
        """
        Generate all the required META parameters
        for building the Anthill
        """
        self.action_map = self.gen_action_map()
        print(":::::::::::::", self.action_map)
        self.lookup_map = self.gen_lookup_map()
        print(":::::::::::::", self.lookup_map)
        self.adj_list = self.gen_adj_list()
        print(":::::::::::::", self.adj_list)

        return nmt(
            self.action_map,
            self.lookup_map,
            self.adj_list
        )

    def transform(self):
        """
        Transform the nest into engine understandable blueprint
        for building the anthill
        """
        if not self.is_valid():
            return
        return self.generate()
