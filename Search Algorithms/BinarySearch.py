# Iterative Solution - Two Pointer Approach
def binary_search(numbers_list, number_to_find):
    left_index = 0                      # Would need to keep track of left and right indices, coz size of array keeps varying
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

# Recursive Solution - Two Pointer Approach
def binary_search_recursive(numbers_list, number_to_find,left_index,right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index]

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

# Initially when the above function is called, left_index should be 0, and right_index should be len(numbers_list)-1.
# That is, binary_search_recursive(numbers_list, number_to_find , 0 , len(numbers_list)-1)