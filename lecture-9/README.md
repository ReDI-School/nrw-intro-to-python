# Error Handling

- Syntax Errors
- Exceptions
- Handling Exceptions
- Raising Exceptions
- Exception Chaining
- User-defined Exceptions

Exception Object contains the **Description** and a **Traceback** to see where the error occurred.

## Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:

```python
# SyntaxError: invalid syntax
while True print('Hello world')
```

## Exceptions

Errors detected during execution are called exceptions and are not unconditionally fatal

```python
# ZeroDivisionError: division by zero
10 * (1/0)

# NameError: name 'spam' is not defined
4 + doesnotexsist*3

# TypeError: Can't convert 'int' object to str implicitly
'2' + 2
```

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

```python
# Base classes
BaseException
Exception
ArithmeticError

# Concrete
SyntaxError

ZeroDivisionError
NameError
TypeError

AssertionError
ImportError
IndexError
NotImplementedError
```

## Example

```python
with open("x_files.txt") as xf:
    the_truth = xf.read()
 
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: 'x_files.txt'

1/0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

1 + 2 + "three"
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(math.sqrt(-1))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'math' is not defined

import math
print(math.sqrt(-1))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: math domain error
```

## Handling Exceptions

The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.
The `finally` block lets you execute code, regardless of the result of the try- and except blocks.

### Syntax

```python
try:
  print(x)
except:
  print("An exception occurred")
  raise
```

## Raising Exceptions

The `raise` statement allows the programmer to force a specified exception to occur.

```python
raise NameError('HiThere')
```

## Exception Chaining

The `raise` statement allows an optional from which enables chaining exceptions by setting the __cause__ attribute of the raised exception. 

```python
try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc
```

## User-defined Exceptions

Programs may name their own exceptions by creating a new exception class (see [Classes from Lecture 8](/lecture-8/) more about Python classes). 

Exceptions should typically be derived from the Exception class, either directly or indirectly.

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
```

## Resources

![Youtube: Exceptions in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=nlCKrKGHSSk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=32)

- [w3schools: Python Error Handling](https://www.w3schools.com/python/gloss_python_error_handling.asp#:~:text=When%20an%20error%20occurs%2C%20or%20exception%20as%20we,raise%20an%20error%2C%20because%20x%20is%20not%20defined%3A)
- [docs.python: Errors](https://docs.python.org/3/tutorial/errors.html)

# Logging

Purpose: Record progress and problems.
Levels: Debug, Info, Warning, Error, Critical.

```python
import logging

# Get info about logging
dir(logging)

# Create logger
logging.basicConfig(level - logging.DEBUG)
logger = logging.getLogger()

# Levels
print(logger.level)

# Use the logger
logger.log("Log message")

logger.error(err)
```

## Resources

- [Youtube: Logging in Python || Learn Python Programming (Computer Science)](https://www.youtube.com/watch?v=g8nQ90Hk328&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=17)


# Error & Logging usage

see [main.py](main.py).


# Testing

```python
import unittest
from test import support

class MyTestCase1(unittest.TestCase):

    # Only use setUp() and tearDown() if necessary

    def setUp(self):
        ... code to execute in preparation for tests ...

    def tearDown(self):
        ... code to execute to clean up after tests ...

    def test_feature_one(self):
        # Test feature one.
        ... testing code ...

    def test_feature_two(self):
        # Test feature two.
        ... testing code ...

    ... more test methods ...

class MyTestCase2(unittest.TestCase):
    ... same structure as MyTestCase1 ...

... more test classes ...

if __name__ == '__main__':
    unittest.main()
```


## Example


```python
import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
```

The unittest module can be used from the command line to run tests from modules, classes or even individual test methods:

```shell
# Test the whole module, a module == file (in this case)
python3 -m unittest test_module

# Test only one class in the module
python3 -m unittest test_module.TestClass

# Test only one function in one class in the module
python3 -m unittest test_module.TestClass.test_method
```

## py.test

py.test is a no-boilerplate alternative to Python’s standard unittest module.

```shell
pip install pytest
```

```python
# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5
```

## Resources

![Youtube: Unit Tests in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=1Lfv5tUGsn8&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=31)

- [docs.python: test](https://docs.python.org/3/library/test.html)
- [docs.python: unittest](https://docs.python.org/3/library/unittest.html)
