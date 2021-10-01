number = float(input('What is your number?'))

if number % 5 == 0 and number % 3 == 0: 
    print ('FIZZ BUZZ')
elif number % 5 == 0:
    print('BUZZ')
elif number % 3 == 0:
    print('FIZZ')
else:
    print(f'{number}')

    
# if you want to loop through a range of number (input parameter = range)    
#
#range = float(input('What is your range?'))
#
# for number in range(1,range):
#     if number % 5 == 0 and number % 3 == 0: 
#         print ('FIZZ BUZZ')
#     elif number % 5 == 0:
#         print('BUZZ')
#     elif number % 3 == 0:
#         print('FIZZ')
#     else:
#         print(f'{number}')