class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
            h = 0
            l = len(arr)
            for i in range(0, l):
                if arr[i]>h:
                    h = arr[i]
            if h in arr:
                 return arr.index(h)