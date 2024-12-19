class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(nums: List[int], lo: int, hi: int, target: int) -> int:
            if hi - lo >= 1:
                mid: int = lo + (hi - lo) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(nums, mid + 1, hi, target)
                else:
                    return binary_search(nums, lo, mid, target)

            else:
                return -1

        return binary_search(nums, 0, len(nums), target) 

       
# [-1,0,3,5,9,12] t=9
# [-1,0,3,5,9,12] t=2
# [5] t=5
# [2,5] t=2
# [-1,0,5] t=5 
