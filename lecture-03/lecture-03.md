# Basic Data Types

# Variables

A variable stores all kinds of data types like `int`, `lists` and even `objects`.
If you create a variable you give it a proper name like `my_interesting_var` and assign a value with `=` and the value of your choice:
`my_interesting_var = 5`

If you want to check what your variable holds you can just print it out: `print(my_interesting_var)` --> `5`

- In python you use `_` underscore to separate out distinct words in variables (snake_case) --> `my_var`. Do not use camelCase like `myVar` for your variables. (It is not Pythonic!).
- You can but you don't have to define the data type the variable is holding --> `my_var: int = 5` or `my_var = 5` is correct

<span style="color:red">Your good friend Luca told you his age is 42. Please create a variable with a proper name and assign his age to it.
Then print it out with the `print` statement.</span>

You can as well check the type of a variable by calling the `type()`function --> `type(my_interesting_var) --> <class 'int'>`

## None

If you don't want to assign any value you can just say `a = None`. You can then assign a proper value later on.

## Numbers

### Integer (int)

Whole numbers positive or negative does not matter:

- `a: int = 1`
- `b: int = 24234245346456475675674534234234`
- `c: int = -3`
- `d: int = 0`

### Float (float)

Floating point numbers that can be positive or negative but always contain one or more decimals:

- `a: float = 1.1`
- `b: float = 2423.393939393`
- `c: float = -3.903`
- `d: float = 0.99`

You can use `e` for the power of 10: x: float = -44.3e20

### Complex (complex)

Complex numbers have a real and a imaginary part sperated by `j`:

- `a: complex = 1j` (0 = real and 1 = imaginary)
- `b: complex = 2+3j` (2 = real and 3 = imaginary)

You can access each part by calling e.g. `print(a.real) and print(a.imag)`  
<span style="color:red">Please assign `5-5j` to a variable `a` and print both parts</span>

### Type Conversion

You can change the type to another by calling the following methods:

- `int()`for integers
- `float()` for floating point values
- `complex()` for complex data types

```Python
my_awesome_var: int = 5
print(my_awesome_var) --> 5
print(float(my_awesome_var) --> 5.0
```

<span style="color:red">What happens if you change a `float` to an `int`?</span>

You can't change a complex number to `int` or `float`!

## Boolean

A boolean (`bool`) describes the truth value of an expression.
It can only be `True` or `False`.
You can convert to bool by calling the `bool()`methode.

- `print(5 == 5)` --> True
- `print(5 > 6)` --> False

<span style="color:red">What is the outcome of `print(bool(0))` and why?</span>

## Strings (str)

Strings hold text and you always need to put it between quotes:

```Python
my_text: str = 'I have a dream'
your_text: str = "I'd like to have 42 beer please"
```

If you use single or double quote is up to you but please be consistent once you decided.
If you use single quotes be aware that you need to escape `'` in text with `\`:

```Python
my_text: str = 'I'd like to have 42 beer please'  <-- This will not work - why?
your_text: str = 'I\'d like to have 42 beer please'
```

If you have a lot of text to write you can use 3 quotes to open and 3 quotes to close.
The linebreaks are the same as in the code.

```Python
my_long_text: str = '''
Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque!
'''
```

### String modifications

For this task please use google ;)

```Python
my_var: str = 'all caps would be great' # Make all upper case
my_var_I_forgot_about: str = 'WHaT iS THis?' # Make all lower case
my_other_var: str = 'manchester' # We need a capital first letter here
some_var: str = 'A house is on fire' # Replace the h with a m
```

### Merge strings and variables

A simple way to merge two strings is with a `+`:

```Python
my_var: str = 'I like big'
your_var: str = 'guts'

merged_text: str = my_var + your_var # Well we are missing sth --> please try this
```

Another way is with `format()` and `{}`:

```Python
your_age: int = 42
my_text: str = 'You are {} years old'
print(my_text.format(your_age))
```

You can add as many `{}` and values as you wish. And of course you can map the value to the `{}` with giving them the correct index number:

```Python
your_age: int = 42
age_tye: str = 'years'
my_text: str = 'You are {1} {0} old'
print(my_text.format(age_tye, your_age))
```

I recommend using `f-strings` (Format Strings):

```Python
your_age: int = 42
age_tye: str = 'years'
my_text: str = f'You are {your_age} {age_tye} old'
print(my_text)
```

Just add a `f` at the beginning of your string and set the correct variables into `{}`.
