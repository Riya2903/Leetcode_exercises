class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set(nums)
        res = list(s)
        k = len(res)
        nums.clear()
        nums.extend(res)
        nums.sort()
        return k