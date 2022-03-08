class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = len(nums)
        s = set(nums)
        if len(s) != l:
            return True