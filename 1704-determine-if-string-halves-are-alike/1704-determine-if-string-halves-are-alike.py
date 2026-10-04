class Solution(object):
    def halvesAreAlike(self, s):
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        count1 = 0
        count2 = 0
        for char in left:
            if char in "aeiouAEIOU":
                count1 += 1
        for char in right:
            if char in "aeiouAEIOU":
                count2 += 1
        return count1 == count2

