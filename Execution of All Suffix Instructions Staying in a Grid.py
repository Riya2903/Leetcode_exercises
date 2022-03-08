class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        def ex(i, j, k): 
                
                if k == len(s): return 0 
                if s[k] == 'L': j -= 1
                elif s[k] == 'R': j += 1
                elif s[k] == 'U': i -= 1
                else: i += 1
                if 0 <= i < n and 0 <= j < n: return 1 + ex(i, j, k+1)
                return 0 

        return [ex(*startPos, k) for k in range(len(s))]