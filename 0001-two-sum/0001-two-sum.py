class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i,n in enumerate(nums):
            req = target-n
            if req in hashMap:
                return [i,hashMap.get(req)]
            hashMap[n] = i

        return []