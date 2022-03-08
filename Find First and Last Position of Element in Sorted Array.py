
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=[]
        l = len(nums)
        for i in range(0,l):
            if nums[i] == target:
                
                c.append(i)
                continue
        l = len(c)
        if l == 0:
            return [-1,-1]
        else:
            b = c[len(c)-1]
            a = c[0]
            return[a,b]