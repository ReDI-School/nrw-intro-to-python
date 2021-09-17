max_number = int(input('Calculate factorial of'))

factorial = 1

for i in range(1, max_number + 1):
    factorial *= i  # shorthand for: factorial = factorial * i

print(f'{max_number}! = {factorial}')
