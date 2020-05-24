from anthill.src.topology.topology import Anthill


class Nest:
    """
    Class to handle all operations on nest including build and execution
    """
    instance = None

    def __init__(self, nest, _dir):
        self.nest = nest
        self._dir = _dir

    def build(self):
        self.instance = Anthill(nest=self.nest).build()

    def run(self):
        Anthill.run(
            instance=self.instance,
            _dir=self._dir
        )
