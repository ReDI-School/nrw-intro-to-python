my_random_numbers = [2, 6, 7, 10, 11, 15]

filtered_list = [
    x
    for x in my_random_numbers
    if x % 3 == 0 or (x - 1) % 5 == 0   # note the brackets around (x-1), since modulo operator takes precedence!
]
print(filtered_list)