class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(0,len(nums)+1):
            if i<len(nums) and i != nums[i]:
                return i
        return i
        