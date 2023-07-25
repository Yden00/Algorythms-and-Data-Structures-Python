from typing import List

def tim_sort(nums: List[int]) -> List[int]:
    n = len(nums)
    def find_min_run(nums: List[int]) -> int:
        if n < 64:
            return n
        else:
            if '1' in bin(n)[7:]:
                return int(bin(n)[:7] + '1', 2)
            else:
                return int(bin(n)[:7], 2)
    minrun = find_min_run(nums)
    run = []

    def insertion_sort(nums: List[int], left: int, right: int) -> List[int]:
        for i in range(left + 1, right + 1):
            element = nums[i]
            j = i - 1
            while element < nums[j] and j >= left:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = element
        return nums

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

print(tim_sort(list(range(10000, 0, -1))))