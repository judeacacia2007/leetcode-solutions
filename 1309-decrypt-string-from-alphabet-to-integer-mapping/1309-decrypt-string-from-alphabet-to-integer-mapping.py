class Solution(object):
    def freqAlphabets(self, s):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                num = int(s[i:i+2])
                result += alphabet[num - 1]
                i += 3
            else:
                num = int(s[i])
                result += alphabet[num - 1]
                i += 1
        return result
        