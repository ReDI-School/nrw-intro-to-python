base = float(input('What is your base?'))
exp = float(input('What is your exponent?'))

num = exp
result = 1
while num > 0:
    result = result * base
    num = num - 1
print(f'{base} raised to the power of {exp} is: {result}')