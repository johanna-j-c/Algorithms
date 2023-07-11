def kth_missing_positive_number(numbers, k):
    '''
    INPUT: List of positive numbers in increating order & a positive integer k
    OUTPUT: The kth missing number
    '''

    missing_nums = []
    z = numbers[len(numbers)-1]+k +1
    
    for num in range(1,z):
        if num in numbers:
            continue
        else:
            missing_nums.append(num)
            
    return missing_nums[k-1]

# list = [2,3,4,7,11]
# k = 5
# expect 9
list = [1,2,3,4]
k = 2
# expect 6
print(kth_missing_positive_number(list,k))