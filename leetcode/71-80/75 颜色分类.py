class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        zore = 0
        one = 0
        two = 0
        for num in nums:
            if num == 0:
              zore = zore + 1
            elif num == 1:
              one = one + 1
              pass
            elif num == 2:
              two = two + 1
              pass
        for i in range(zore):
            print(i)
            nums[i] = 0
        for i in range(zore, zore + one):
            print(i)
            nums[i] = 1
        for i in range(zore + one, zore + one + two):
            print(i)
            nums[i] = 2
        print(nums)

s = Solution()
s.sortColors([2,0,2,1,1,0])