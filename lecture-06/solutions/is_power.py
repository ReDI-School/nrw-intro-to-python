import math

is_power = lambda x, y : math.log(x, y).is_integer()
print(is_power(9,3))
print(is_power(16,2))
print(is_power(16,4))