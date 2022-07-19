import re
# Solve the following problem:
# In comments Provide the Time Complexity of your solution.
# Your mission is to solve this problem in O(n) time or better

# A phrase is a  if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return truefalse.
 
def palindrome(s):
    l,h = 0, len(s) - 1
      
    while l <= h:
        if not(s[l] >= 'a' and s[l] <= 'z'):
            l += 1
        elif not(s[h] >= 'a' and s[h] <= 'z'):
            h -= 1
        elif s[l] == s[h]:
            l += 1
            h -= 1
        else:
            return False
    return True
    
s = "A man, a plan, a canal: Panama"
s = re.sub(r'[^a-zA-Z0-9]', '', s)
s = s.lower()

if (palindrome(s)):
     print ("Sentence is palindrome.")
else:
     print ("Sentence is not palindrome.")

print(s)


# see images folder to see explanation 

# the other "palindromes" copy and paste these in the s= part 
# s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
