from typing import List

def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    mid = nums[len(nums) // 2]
    left = list(filter(lambda x: x < mid, nums))
    same = [i for i in nums if i == mid]
    right = list(filter(lambda x: x > mid, nums))
    return quick_sort(left) + same + quick_sort(right)



