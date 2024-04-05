import random, time
from test import quick_sort

class UnequalListException(Exception):
    pass

def create_nums(amount, limit=(-10000, 10000)):
    ret = []
    for i in range(amount):
        ret.append(random.randint(limit[0], limit[1]))
    return ret

def stopwatch(func, *args):
    start_time = time.time()
    returnval = func(*args)
    end_time = time.time()
    return end_time - start_time, returnval

sim_amount = int(input('How many simulations? '))
len_amount = int(input('How many numbers per list? '))

for i in range(sim_amount):
    list_of_nums = create_nums(len_amount)

    sorted_time, sorted_list = stopwatch(sorted, list_of_nums)
    print('Sort() took %s' % round(sorted_time, 5))
    sissis_time, placeholder = stopwatch(quick_sort, list_of_nums, 0, len(list_of_nums) - 1)
    print('quick_sort() took %s' % round(sissis_time, 5))
    
    if sorted_list != list_of_nums:
        raise UnequalListException
