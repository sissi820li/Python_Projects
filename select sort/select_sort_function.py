def select_sort(list_of_numbers): 
    spot = 0
    counter = 0
    
    for number in range(len(list_of_numbers)):
        smallest_number = list_of_numbers[number]
        final_index = number
        for index in range(number + 1, len(list_of_numbers)):
            counter = counter + 1 
            if smallest_number > list_of_numbers[index]:
                smallest_number = list_of_numbers[index]
                final_index = index
                    
        if final_index == spot:
            list_of_numbers[int(final_index)] = list_of_numbers[int(final_index)]
        else:
            list_of_numbers[spot], list_of_numbers[int(final_index)] = list_of_numbers[int(final_index)], list_of_numbers[spot]

        spot = spot + 1

    return counter

