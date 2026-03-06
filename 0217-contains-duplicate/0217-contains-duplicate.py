from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cnter = Counter(nums)
        for cnt in cnter.values():
            if cnt>=2:
                return True
        return False