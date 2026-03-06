class Solution:
    def findMin(self, nums: List[int]) -> int:
        minElem = float('inf')
        low = 0
        high = len(nums)-1

        while (low<=high):
            mid = low + (high-low)//2
            if nums[low]<=nums[mid]:
                minElem = min(minElem,nums[low])
                low = mid+1
            else:
                minElem = min(minElem,nums[mid])
                high = mid-1
        return minElem