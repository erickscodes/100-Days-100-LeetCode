# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove all non characters (including spaces) / lower case the character
        filtered = ""
        filteredBackwards = ""
        for i in range(len(s)):
            # if the character is part of the alphabet push it into the temp
            if s[i].isalpha():
                filtered += s[i].lower()
            #  if the character is a digit 
            if s[i].isdigit():
                filtered += s[i]
        for i in range(len(filtered) - 1, -1, -1):
            # loop through filtered string backwards and add it to the string 
            filteredBackwards += filtered[i]
        # return if it is equal to each other 
        return filtered == filteredBackwards
    