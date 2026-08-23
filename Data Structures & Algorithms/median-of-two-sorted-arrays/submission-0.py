from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        # We always want A to be the smaller array for efficiency!
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # Partition for A
            j = half - i - 2  # Partition for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Did we find the perfect partition?
            if Aleft <= Bright and Bleft <= Aright:
                # If total length is odd, the median is the smallest right element
                if total % 2:
                    return min(Aright, Bright)
                # If even, it's the average of the biggest left and smallest right
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Need to shift our partition to the left
            elif Aleft > Bright:
                r = i - 1
            # Need to shift our partition to the right
            else:
                l = i + 1