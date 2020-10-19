
def get_max_val_index(list_of_numbers):
    
    list_of_indices = []
    n = len(list_of_numbers)

    max_val = max(list_of_numbers)
    
    first_index = list_of_numbers.index(max_val,0,n)
    list_of_indices.append(first_index)
    
    if (n-first_index) > 0:
        for idx in range(first_index+1,n):
            if list_of_numbers[idx] == max_val:
                list_of_indices.append(idx)
                
    return list_of_indices


def get_average(list_of_numbers):
    return sum(list_of_numbers)/len(list_of_numbers)


def get_standard_deviation(list_of_numbers):
    average = get_average(list_of_numbers)
    sum_ = 0.0
    for item in list_of_numbers:
        sum_ += (item-average)**2
    variance = sum_/(len(list_of_numbers)-1)
    standard_deviation = variance**0.5
    return standard_deviation
    
    
    