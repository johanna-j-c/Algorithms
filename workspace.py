# str1 = "ABABAB"
# str2 = "ABAB"

# print(str2[0:-2])
# print(str1[-2:])

def gcdOfStrings(str1, str2):
        l = ""
        s = ""
        if len(str2) > len(str1):
            l = str2
            s = str1
        else:
            l = str1
            s = str2

        i = len(s)
        k = len(l)
        if s in l and l[i:] == s:
            return s
        elif s not in l[:i]:
            return ""
        
        j = 1
        i -= 1
        while i > 0:
            k = len(l[-j:])
            if l[-j:] == s[0:k]:
                return s[0:k]
            j += 1
            i -= 1

# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# str1 = "AAAAAAAAA"
# str2 = "AAACCC"
str1 = "ABCDEF"
str2 = "ABC"

print(gcdOfStrings(str1, str2))

# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         l = ""
#         s = ""
#         if len(str2) > len(str1):
#             l = str2
#             s = str1
#         else:
#             l = str1
#             s = str2

#         i = len(s)
#         if s in l and l[i:] == s:
#             return s
#         j = 1
#         i -= 1
#         while i > 0:
#             k = len(l[-j:])
#             if l[-j:] == s[0:k]:
#                 return s[0:k]
#             j += 1
#             i -= 1
        
#         return ""