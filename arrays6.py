# Given a nested array, "flatten" the array, so that all values are in a one-dimensional array. Feel free to return a new array. Don't forget your edge cases!

# Example Input: [ 1, [ 2, 3 ], 4, [ ] ]
# Example Output: [ 1, 2, 3, 4 ]

# Example Input: [ 1, [ 2, 3 ], 4, [ 5, 6, 7 ] , [ 8 ] ]
# Example Output: [ 1, 2, 3, 4, 5, 6, 7, 8 ]

# Now, try "flattening" in-place

# def flatten_array(array):
#     flattened_array = []

#     for x in array:
#         if not isinstance(x, list):
#             flattened_array.append(x)
#         else:
#             for y in x:
#                 if x:
#                     flattened_array.append(y)
    
#     return flattened_array

# modify the original array
def flatten_array(array):
    flattened_array = []

    for x in array:
        if not isinstance(x, list):
            flattened_array.append(x)
        else:
            for y in x:
                if x:
                    flattened_array.append(y)
    
    return flattened_array

list1 = [ 1, [ 2, 3 ], 4, [ ] ]

list2 = [ 1, [ 2, 3 ], 4, [ 5, 6, 7 ] , [ 8 ] ]

print(flatten_array(list1))
print(flatten_array(list2))

# Time complexity: O(n), linear where n is the total amount of numbers in the nested array structures
# Space complexity: O(n), linear in respect to the total amount of numbers in the original array











# Given an array with random numbers, remove duplicates. Return a new array. Don't forget your edge cases!

# Example Input: [ 1, 2, 1, 5, 1, 1, 3 ]
# Example Output: [ 1, 2, 5, 3 ]

# Now, try removing duplicates in-place

def remove_duplicates(array):
    for x in array:
        for y in array:
            if y == x:
                array.pop(y)
    return array

list1 = [ 1, 2, 1, 5, 1, 1, 3 ]
# print(remove_duplicates(list1))