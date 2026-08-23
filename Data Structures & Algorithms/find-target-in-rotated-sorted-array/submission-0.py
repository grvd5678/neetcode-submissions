from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] == target:
                return mid

            # Check if the Left portion is strictly sorted
            if nums[l] <= nums[mid]:
                # Is the target outside this sorted left portion?
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # Otherwise, it must be inside this portion!
                else:
                    r = mid - 1
            
            # Otherwise, the Right portion must be strictly sorted
            else:
                # Is the target outside this sorted right portion?
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # Otherwise, it must be inside this portion!
                else:
                    l = mid + 1

        return -1