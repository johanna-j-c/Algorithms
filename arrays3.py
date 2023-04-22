# 1
# Given an array, reverse the order of values without using the built-in method reverse or slice, 
# ie. [: :-1]. Return the same array. Don't forget edge cases!

# Example Input: [1, 2, 3, 4, 5, 6]
# Example Output: [6, 5, 4, 3, 2, 1]

def reverse_array(list):
    end_of_list = -1
    for i in range(len(list) // 2):
        to_be_swapped1 = list[end_of_list]
        to_be_swapped2 = list[i]
        list[i], list[end_of_list] = to_be_swapped1, to_be_swapped2
        end_of_list -= 1
    return list

# example_list = [1, 2, 3, 4, 5, 6]
# example_list2 = [8, 9, 10, 11, 12, 13, 14, 15]
# print(reverse_array(example_list))
# print("**********************")
# print(reverse_array(example_list2))



# 2
# Given an array and number, rotate the values of the array to the right by that number. 
# Don't use slice. Return the same array. Don't forget edge cases!
# Example Input: [1, 2, 3, 4, 5], 2
# Example Output: [4, 5, 1, 2, 3]

# Example Input: [1, 2, 3, 4, 5], 5
# Example Output: [1, 2, 3, 4, 5]

# EXTRA CHALLENGE
# Try shifting to the left instead

def rotate_array(list):
    last_value = list[-1]
    i = len(list)-1
    while i > 0:
        list[i] = list[i-1]
        i -= 1
    list[0] = last_value


print(rotate_array([1, 2, 3, 4, 5], 2))
print('*********************')
print(rotate_array([1, 2, 3, 4, 5], 5))
