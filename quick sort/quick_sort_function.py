def sort_list(list_of_numbers, start, end):
    pivot = start
    
    for i in range(start+1, end+1):
        if list_of_numbers[i] <= list_of_numbers[start]:
            pivot += 1
            list_of_numbers[i], list_of_numbers[pivot] = list_of_numbers[pivot], list_of_numbers[i]
    list_of_numbers[pivot], list_of_numbers[start] = list_of_numbers[start], list_of_numbers[pivot]

    return pivot

def quick_sort(list_of_numbers, start, end):
    if start >= end:
        return
    
    pivot = sort_list(list_of_numbers, start, end)
    
    quick_sort(list_of_numbers, start, pivot-1)
    quick_sort(list_of_numbers, pivot+1, end)
