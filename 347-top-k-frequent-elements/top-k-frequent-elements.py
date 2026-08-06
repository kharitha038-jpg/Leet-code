from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        count=Counter(nums)
        count=sorted(count,key=count.get,reverse=True)
        return count[:k]
        