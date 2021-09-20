n = int(input('n='))

i = 2
while n > 1:
    if n % i == 0:
        print(i)
        n = n / i
        i = 2
    else:
        i += 1