def insert_sort(original_list, sorted_list):

    sorted_list.append(original_list[0])
    del original_list[0]
    
    for number in original_list:

        index = 0
        first_range = 0
        last_range = int(len(sorted_list)) - 1

        while last_range - first_range > 0:   
            index = int((first_range + last_range)/2)

            if number < sorted_list[index]:
                last_range = int(index)
                
            else:
                first_range = last_range - int(last_range - first_range)/2

        index = int((first_range + last_range)/2)
 
        if number > sorted_list[index]:
            final_index = index + 1

        else:
            final_index = index


        sorted_list.insert(final_index, number)        

