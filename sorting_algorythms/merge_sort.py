from typing import List

def merge_sort(nums: List[int]) -> List[int]:
    def fmerge(nums1: List[int], nums2: List[int]) -> List[int]:
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i < len(nums1):
            result += nums1[i:]
        if j < len(nums2):
            result += nums2[j:]
        return result
    if len(nums) <= 1:
        return nums
    middle = len(nums) // 2
    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return fmerge(left, right)

