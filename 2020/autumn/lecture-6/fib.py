from time import time


def my_range(start, stop):
    i = start

    while i < stop:
        yield i
        i += 1


my_list = my_range(1, 1000000)

for i in my_list:
    if i > 100:
        break

    print(i)


KNOWN_SEQUENCE = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55)


def validate_fib_fn(fn):
    """Validate the given Fibonacci function works as expected."""
    # Loop over each of the numbers in the sequence above
    for i, expected in enumerate(KNOWN_SEQUENCE):
        # Calculate the actual value generated for this number by our function
        actual = fn(i + 1)
        # Assert that it matches our expectation
        assert (
            actual == expected
        ), f"fib({i + 1}) incorrect. Expected: {expected}. Actual: {actual}."

    # If we've reached here, all is well!
    print("Given function works as expected!")


def print_fib_sequence(fn, until=10):
    """Print out the Fibonacci numbers using the given function.

    Once complete, print out the time it took to generate the sequence.

    """
    print("Fibonacci Sequence")
    print("==================")
    assert until <= 100, "Cannot go beyond 100"

    # Capture the time before we start to generate the sequence
    start = time()

    # Start generating the sequence
    for i in range(1, until + 1):
        print(f"{fn(i)}, ", end="")

    # Calculate the time it took to run generate the sequence
    duration_seconds = time() - start
    print("\n------------------")
    print(f"Time taken: {duration_seconds:.3f} seconds")


def fib_recursive(n):
    """Return the nth number in the Fibonacci sequence."""
    if n > 1:
        return fib_recursive(n - 1) + fib_recursive(n - 2)
    else:
        return n


def fib_recursive_debug(n, indent=0):
    """Return the nth number in the Fibonacci sequence."""
    print(("  " * indent) + "fib_recursive(" + str(n) + ")")

    if n > 1:
        return fib_recursive_debug(
            n - 1, indent=indent + 1
        ) + fib_recursive_debug(n - 2, indent=indent + 1)
    else:
        return n


def gen_fibs():
    """Generate the fibonacci sequences from 0."""
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def fib_using_generator(x):
    for n, fib_n in enumerate(gen_fibs()):
        if n == x:
            return fib_n


def fib_recursive_cached(n):
    """Return the nth number in the Fibonacci sequence."""
    cache = {}

    def inner(i):
        if i not in cache:
            if i > 1:
                cache[i] = inner(i - 1) + inner(i - 2)
            else:
                cache[i] = i

        return cache[i]

    return inner(n)
