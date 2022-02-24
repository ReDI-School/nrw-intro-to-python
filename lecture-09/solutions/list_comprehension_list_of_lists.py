my_solution = [
    e
    for l in list_of_lists
    for e in l[:2]  # only consider the first and second position
    if e % 2 == 0  # only consider even numbers
]
print(my_solution)