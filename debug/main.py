"""
Debug functions for zebra puzzle solver
"""


def instrument_fn(fn, *args):
    """
    Debug
    """
    c.starts, c.items = 0, 0
    result = fn(*args)
    print("{0} got {1} with {2} iterations"
          "over {3} items".format(fn.__name__, result, c.starts, c.items))


def c(sequence):
    """
    Generate items in sequence; keeping counts as we go.
    c.starts is the number of sequences started.
    c.items is the number of items generated.
    """
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item
