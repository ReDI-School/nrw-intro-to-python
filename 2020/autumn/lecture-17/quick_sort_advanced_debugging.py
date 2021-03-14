"""
This module shows a more advanced debugging option, which we can use on
recursive functions. The benefit of this decorator, is that it "pads" the
nested calls, so that we can see how our function goes deeper before resolving
the values and generating the final result.
"""


def _print_padded(string, depth):
    """Print a string prefixed with spaces, given by the "depth"."""
    padding = "  " * depth if depth else ""
    print(f"{padding}{string}")


def _print_call(fn, args, kwargs, depth=0):
    """Print the function call signature. Pad the string using the depth."""
    # Get the name of the function
    fn_name = fn.__name__

    # Convert all of the "args" to strings
    args_repr = [str(a) for a in args]

    # Convert all of the "kwargs" to strings
    kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]

    # Combine all of our arg and kwarg strings
    signature = ", ".join(args_repr + kwargs_repr)

    # Print out the function signature, as if we did it ourselves
    _print_padded(f">>> {fn_name}({signature})", depth)


def debug_recursion(fn):
    """Debug a recursive function.

    This prints out the recursive function calls and the results, and each
    time we get deeper into our recursive calls, we "pad" the string to
    make it clearer.
    """
    depth = 0

    def replacement(*args, **kwargs):
        # Use the depth variable in the parent function
        nonlocal depth

        # Print the function being called
        _print_call(fn, args, kwargs, depth)

        # Track the depth before and after we call the function
        # We'll use this to pad out our debug information
        depth += 1
        result = fn(*args, **kwargs)
        depth -= 1

        # Print out all of the intermediate results
        if depth != 0:
            _print_padded(result, depth)

        return result

    return replacement


@debug_recursion
def quick_sort(collection: list) -> list:
    """A pure Python implementation of quick sort algorithm
    :param collection: a mutable collection of comparable items
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, 5, 0, -45])
    [-45, -2, 0, 5]
    """
    if len(collection) < 2:
        return collection
    pivot = collection.pop()  # Use the last element as the first pivot
    greater = []  # All elements greater than pivot
    lesser = []  # All elements less than or equal to pivot
    for element in collection:
        (greater if element > pivot else lesser).append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


print(quick_sort([2, 1, 4, 3]))
# quick_sort([2, 1, 4, 3])
# -> quick_sort([2, 1]) + [3] + quick_sort([4])
# -> [1] + quick_sort([2]) + [3] + [4]
# -> [1] + [2] + [3] + [4]
