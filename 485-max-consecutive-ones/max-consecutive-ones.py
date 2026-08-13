class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        mm=0
        c=0
        for i in nums:
            if i == 1:
                c+=1
            else:
                c=0
            mm=max(mm,c)
        return mm