from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        s=nums1 if len(nums1)<len(nums2) else nums2
        count=Counter(s)
        y=nums2 if len(nums2)>len(nums1) else nums1
        result =[]
        for i in range (len(y)):
            if y[i] in count :
                count[y[i]]-=1
                result.append(y[i])
                if count [y[i]]<=0:
                    del count[y[i]]
        return result


      
        