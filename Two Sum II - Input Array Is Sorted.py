class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       second={}
       for i, value in enumerate(numbers):
           rem = target - numbers[i]
           
           if rem in second:
               return [second[rem]+1, i+1]
            
           second[value]=i