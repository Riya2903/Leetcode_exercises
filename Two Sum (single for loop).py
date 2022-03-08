class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       
            
       second={}
       for i, value in enumerate(nums):
           rem = target - nums[i]
           
           if rem in second:
               return [i, second[rem]]
            
           second[value]=i