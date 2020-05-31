class Solution:
    def twoSum(self, nums: List[int], target: int):
        targetMap = {}
        for index, num in enumerate(nums):
          key = target - num
          if key in targetMap:
            return [targetMap[key], index]
          targetMap[num] = index