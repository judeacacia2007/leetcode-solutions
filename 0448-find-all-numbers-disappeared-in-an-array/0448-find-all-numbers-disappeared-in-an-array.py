class Solution(object):
    def findDisappearedNumbers(self, nums):
        present = set(nums)
        missing = []

        for num in range(1, len(nums) + 1):
            if num not in present:
                missing.append(num)

        return missing