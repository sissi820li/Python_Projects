from prime_number_tester_function import prime_number_tester as pmt

user_number = int(input('Enter a number: '))
#pmt(user_number)

is_prime_number, counter = pmt(user_number)

if is_prime_number == 1:
    print('This number is a prime number.')
    print('Counter: ' + str(counter))
else:
    print('This number is not a prime number.')
    print('Counter: ' + str(counter))
   
   
