class Solution(object):
    def reverseVowels(self, s):
        r = len(s) - 1
        l = 0
        s=list(s)
        while (l<r):
            while s[l] not in "aeiouAEIOU" and l<r:
                l+=1
            while s[r] not in"aeiouAEIOU" and l<r:
                r-=1
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        s="".join(s)
        return s