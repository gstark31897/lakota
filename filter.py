import copy


filters = {}

class Filter:
    def __init__(self, name, ins, outs):
        self.name = name
        self.ins = ins
        self.outs = outs


def make_filter(func):
    ins = copy.copy(func.__annotations__)
    del ins['return']
    outs = func.__annotations__['return']
    name = func.__name__
    filter = Filter(name, ins, outs)
    filters[name] = filter

