class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        numbers = [n ** 2 for n in nums]
        numbers.sort()
        
        return numbers