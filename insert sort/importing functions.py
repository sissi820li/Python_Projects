import random
import time

from insert_sort_function import insert_sort
list_of_numbers = []
list_of_numbers2 = []
list_of_numbers3 = []

user_number = int(input('How many numbers would you like to generate?: '))
for number in range(user_number):
    list_of_numbers.append(random.randint(-100000, 100000))

list_of_numbers2 = list_of_numbers

print('Here is your current list of unsorted numbers: ')
print(list_of_numbers)

start = time.time()
sorted_list = sorted(list_of_numbers)
end = time.time()
final_time = end - start
print('**timer for sort(): ' + '%.3f' % (final_time) + 's**')

start = time.time()
counter = insert_sort(list_of_numbers2, list_of_numbers3)
end = time.time()
final_time = end - start
print(list_of_numbers3)
print('**timer for insert_sort(): ' + '%.3f' % (final_time) + 's**')
print('**counter for insert_sort(): ' + str(counter) + '**')

if list_of_numbers3 == sorted_list:
    print('Insert sort list has been sorted correctly.')
