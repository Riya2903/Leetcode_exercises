class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        
        start=0
        maxLength = 1
        for i in range(l):
            low = i - 1
            high = i + 1
            while (high < l and s[high] == s[i] ):                              
                high=high+1

            while (low >= 0 and s[low] == s[i] ):                
                low=low-1

            while (low >= 0 and high < l and s[low] == s[high] ):
              low = low-1
              high=high+1


            length = high - low - 1
            if (maxLength < length):
                maxLength = length
                start=low+1
        return s[start:start+maxLength]