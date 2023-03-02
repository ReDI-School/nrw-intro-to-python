lower_bound = int(input('Lower bound'))
upper_bound = int(input('Upper bound'))

sum_of_odds = 0
count_of_evens = 0
for i in range(lower_bound, upper_bound + 1):
    if i % 2 == 1:
        sum_of_odds += i
    else:
        count_of_evens += 1

print(f'Sum of odd numbers: {sum_of_odds}')
print(f'Count of even numbers: {count_of_evens}')