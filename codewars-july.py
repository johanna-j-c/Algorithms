def likes(names):
    num = len(names)
    
    if num == 0:
        return "no one likes this"
    elif num == 1:
        return f"{names[0]} likes this"
    elif num == 2:
        return f"{names[0]} and {names[1]} like this"
    elif num == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        diff = num - 2
        return f"{names[0]}, {names[1]} and {diff} others like this"
    
def disemvowel(string_):
    vowels = ["a","A","E","e","I","i","O","o","U","u"]
    for letter in vowels:
        string_ = string_.replace(letter, "")
    return string_

def get_count(sentence):
    vowels = ["a","e","i","o",'u']
    count = 0
    
    for letter in sentence:
        if letter in vowels:
            count += 1
    
    return count

def opposite(number):
        return number*-1

def number_to_string(num):
    return str(num)

# Assume length will be at least 1
# no negative prices
# all int
# just consider max profit, doesn't matter consec duplicates

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    # initiate a var to hold max profit
    max_profit = 0

    # loop through the prices array 
    for i in range(len(prices)):
      for j in range(i,len(prices)):
        diff = prices[j] - prices[i]
        if diff > 0 and diff > max_profit:
          max_profit = diff
    print(max_profit)  
    return max_profit  
  # compare the price of the day with the upcoming days
  # nested loop to acces the price of the upcoming days
  # find the difference
  # the highest day will added to the max profit

  # return the max profit



# prices1 = [7,1,5,3,6,4]
# assert maxProfit(prices1) == 5

# prices2 = [7,6,4,3,1]
# assert maxProfit(prices2) == 0

# prices3 = [3, 10, 10, 1]
# assert maxProfit(prices3) == 7

# prices4 = [2, 10, 4, 2, 8, 10]
# assert maxProfit(prices4) == 8

prices5 = [2]
assert maxProfit(prices5) == 0

print('Test cases passed')

def array_diff(a, b):
    copy_a = a.copy()
    set_b = set(b)
    for num_b in set_b:
        for num_a in a:
            if num_b == num_a:
                copy_a.remove(num_a)
            elif num_b not in a:
                continue
    
    return copy_a