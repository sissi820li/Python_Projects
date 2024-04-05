
def prime_number_tester(number_to_test):
    #first value: return 1 means the user number is a prime number
    #first value: return 0 means the user number is not a prime number
    #second value: how many times user number was tested 
    import math
    counter = 0

    is_prime_number = 1
    
    if number_to_test % 2 == 0:
        counter = counter + 1
        
        #print('Counter: ' + str(counter))
        is_prime_number = 0 
    else:
        biggest_divisor = math.sqrt(number_to_test)
        for divisor in range(3,int(biggest_divisor) + 1,2):
            counter =  counter + 1
            equation_for_remainder = number_to_test % divisor
            if equation_for_remainder == 0:
                is_prime_number = 0
                break
            else:
                is_prime_number = 1

        if is_prime_number == 0:
            #print('Counter: ' + str(counter))
            is_prime_number = 0
        else:
            #print('Counter: ' + str(counter))
            is_prime_number = 1
    return is_prime_number, counter
