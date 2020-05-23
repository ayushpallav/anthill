from anthill.src.topology.topology import Anthill


class Nest:
    """
    Class to handle all operations on nest including build and execution
    """
    instance = None

    def __init__(self, nest):
        self.nest = nest

    def build(self):
        self.instance = Anthill(nest=self.nest).build()

    def run(self):
        pass
