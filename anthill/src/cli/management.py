from anthill.src.topology.transform import TransformNest


class Nest:
    """
    Class to handle all operations on nest including build and execution
    """
    def __init__(self, nest):
        self.nest = nest

    def build(self):
        _nest = TransformNest(nest=self.nest).transform()

    def run(self):
        pass
