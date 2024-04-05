
user_number = int(input('Please enter a number: '))

counter = 0

results = 0

prime_number_total = 1

import math

for all_numbers_to_user_number in range(3,int((user_number)+1),2):
    results = 0
    biggest_divisor = math.sqrt(all_numbers_to_user_number)
    for divisor in range(3,int(biggest_divisor) + 1,2):
        counter =  counter + 1
        equation_for_remainder = all_numbers_to_user_number % divisor
        if equation_for_remainder == 0:
            results = 1
            break
        else:
            results = 0

    if results == 1:
        results = 1
    else:
        #print(str(all_numbers_to_user_number) + ' is a prime number.')
        prime_number_total = prime_number_total + 1

print('There are ' + str(prime_number_total) + ' prime numbers.')

print('counter: ' + str(counter))

