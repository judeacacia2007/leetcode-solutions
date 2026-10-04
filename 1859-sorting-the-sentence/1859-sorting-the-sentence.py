class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        result = [""] * len(words)
        for word in words:
            position = int(word[-1])
            actual_word = word[:-1]
            result[position - 1] = actual_word
        return " ".join(result)

