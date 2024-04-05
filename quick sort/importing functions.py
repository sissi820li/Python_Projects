import random
import time
from quick_sort_function import quick_sort

list_of_numbers = []

user_number = int(input('How many numbers would you like to generate?: '))
for number in range(user_number):
    list_of_numbers.append(random.randint(-10000, 10000))

list_of_numbers2 = list_of_numbers
len_list = len(list_of_numbers)

print('Here is your current list of unsorted numbers: ')
print(list_of_numbers)

start = time.time()
list_of_numbers.sort()
end = time.time()
final_time = end - start
print('**timer for sort(): ' + '%.3f' % (final_time) + 's**')

start = time.time()
counter = quick_sort(list_of_numbers2, 0, len_list - 1)
end = time.time()
final_time = end - start
print(list_of_numbers2)
print('**timer for quick_sort(): ' + '%.3f' % (final_time) + 's**')

if list_of_numbers2 == list_of_numbers:
    print('Quick sort list has been sorted correctly.')
 
