# Write a function reverse that accepts a string text as a parameter. 
# It returns the reverse of text by reversing all characters in the string.

# def reverse(text):
#     if not text:
#         return ""

#     print(text)
    
#     return text[-1] + reverse(text[0:-1])

# print(reverse("cat"))

def is_nested_parens(parens):
    if parens == "":
        return True
    elif parens == "))" or parens == "((":
        return False
    
    return is_nested_parens(parens[1:-1])


print(is_nested_parens("(())))"))