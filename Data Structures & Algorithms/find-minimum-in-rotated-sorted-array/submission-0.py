from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            m = l + ((r - l) // 2)
            
            # If the middle is greater than the right end, 
            # the minimum HAS to be on the right side.
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the right side is sorted, so the minimum 
            # is either at 'm' or somewhere to the left.
            else:
                r = m
                
        # When l == r, we've cornered the minimum element!
        return nums[l]