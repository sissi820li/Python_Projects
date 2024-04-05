import random
import time

from select_sort_function import select_sort

list_of_numbers = []

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
counter = select_sort(list_of_numbers2)
end = time.time()
final_time = end - start
print('**timer for select_sort(): ' + '%.3f' % (final_time) + 's**')
print('**counter for select_sort(): ' + str(counter))

if list_of_numbers2 == sorted_list:
    print('Select sort list has been sorted correctly.')




