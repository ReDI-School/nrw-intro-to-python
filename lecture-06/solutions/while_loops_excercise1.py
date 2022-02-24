S = int(input('Number of of which you want to find the square root'))
guess = float(input(f'Initial guess for square root of {S}'))

next_guess = (guess + S/guess) / 2
while not (-0.001 <= guess - next_guess <= 0.001):
    print(next_guess)
    guess = next_guess
    next_guess = (guess + S/guess) / 2

print(f'Square root of {S} is roughly {guess}')