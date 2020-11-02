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


```python
import logging

# Create logger
logging.basicConfig(level - logging.DEBUG)
logger = logging.getLogger()

# Use the logger
logger.log("Log message")

logger.error(err)
```

## Resources


# Error & Logging usage

see [main.py](main.py).


# Testing


## Resources

![Youtube: Unit Tests in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=1Lfv5tUGsn8&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=31)

- [docs.python: test](https://docs.python.org/3/library/test.html)
- [docs.python: unittest](https://docs.python.org/3/library/unittest.html)
