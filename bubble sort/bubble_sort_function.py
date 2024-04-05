def bubble_sort(list_of_numbers):
    counter = 0 
    for number in range(len(list_of_numbers)):
        for index in range(number + 1, len(list_of_numbers)):
            counter = counter + 1 
            if list_of_numbers[number] > list_of_numbers[index]:
                list_of_numbers[index], list_of_numbers[number] = list_of_numbers[number], list_of_numbers[index]

    return counter

