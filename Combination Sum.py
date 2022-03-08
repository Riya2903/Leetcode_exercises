class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        li =[]
    
        candidates.sort()
        def h(a,s,target,j):
            if s == target:
                if a not in li:
                    li.append(a)
                return
            for i in range(j,len(candidates)):
                if s+candidates[i]>target:
                    return
                h(a+[candidates[i]],s+candidates[i],target,i)
        h([],0,target,0)
        return li
                  