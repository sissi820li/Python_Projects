import random
import time 

list_of_numbers = []

user_number = int(input('How many numbers would you like to generate?: '))
for number in range(user_number):
    list_of_numbers.append(random.randint(-100000, 100000))

print('Here is your current list of unsorted numbers: ')
print(list_of_numbers)

user_response = input('Would you like to sort the list? Enter "yes" or "no": ')
if user_response == 'yes':

    spot = 0

    start = time.time()
    sorted_list = sorted(list_of_numbers)
    end = time.time()
    final_time = end - start
    print('**timer for sort(): ' + '%.3f' % (final_time) + 's**')

    start = time.time()
    for number in range(len(list_of_numbers)):
        smallest_number = list_of_numbers[number]
        final_index = number
        for index in range(number + 1, len(list_of_numbers)):
            if smallest_number > list_of_numbers[index]:
                smallest_number = list_of_numbers[index]
                final_index = index
                    
        if final_index == spot:
            list_of_numbers[int(final_index)] = list_of_numbers[int(final_index)]
        else:
            list_of_numbers[spot], list_of_numbers[int(final_index)] = list_of_numbers[int(final_index)], list_of_numbers[spot]

        spot = spot + 1

    end = time.time()
    final_time = end - start
    print('Here is the sorted list of numbers: ')
    print(list_of_numbers)
    print('**timer: ' + '%.3f' % (final_time) + 's**')

    if list_of_numbers == sorted_list:
        print('The list has been sorted.')
        
        
else:
    quit

