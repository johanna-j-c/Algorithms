# 1
# Given an array and a number n,  return the nth-largest number in the array. Don't forget edge cases!

# Example Input: [5, 8, 1, 3, 7, 5, 6], 3
# Example Output: 6

# Example Input: [3, 1, 5], 5
# Example Output: None

def get_nth_largest_num(array, n):
    # guard clause if n is greater the length of array
    if n > len(array):
        return None

    # re-order the array greatest to smallest
    i = 1
    while i < len(array):
        to_insert = array[i]
        insertion_index = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while insertion_index > 0 and array[insertion_index-1] > to_insert:
            array[insertion_index] = array[insertion_index-1]
            insertion_index -= 1
        array[insertion_index] = to_insert
        i += 1
    print(array)
    
    # find the value at index -3
    return array[-3]

# print(get_nth_largest_num([5, 8, 1, 3, 7, 5, 6], 3))
# print('**********************')
# print(get_nth_largest_num([3, 1, 5], 5))

# 2
# Given an array, a start position, and an end position, remove the 
# values within that start-end range "in-place," then return the original array. 
# Don't use slice. Don't forget edge cases!

# Example Input: [5, 8, 1, 3, 7, 5, 6,10], 3, 6
# Example Output: [5, 8, 1, 10]

# Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 5,7
# Example Output: [4, 5, 6, 7, 10]

# Example Input: [4, 5, 6, 7, 10, 11, 12, 13], 7,11
# Example Output: [4, 5, 6, 7, 10, 11, 12]

