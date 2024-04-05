
user_number = int(input('Please enter a number: '))

counter = 0

results = 0

import math

#print('Counter 1: ' + str(counter))

results = 0


biggest_divisor = int(math.sqrt(user_number) + 2)

#print(biggest_divisor)

for divisor in range(3,biggest_divisor,2):
    
    #print('Counter 2: ' + str(counter))
    
    counter =  counter + 1
    
    #print('Counter 3: ' + str(counter))
    
    equation_for_remainder = user_number % divisor
    if equation_for_remainder == 0:
        results = 1
        break
    else:
        results = 0
        

if results == 1:
    print(str(user_number) + ' is not a prime number.')
    print('Counter: ' + str(counter))
else:
    print(str(user_number) + ' is a prime number.')
    print('Counter: ' + str(counter))
    
