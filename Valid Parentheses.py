class Solution:
    def isValid(self, s: str) -> bool:
      
       while(len(s)!=0):
            if "()" in s :
                    s = s.replace("()", "")
                    continue

            elif "{}" in s:
                    s = s.replace("{}", "")
                    continue

            elif "[]" in s:
                    s = s.replace("[]", "")
                    continue
            else:
                
                break
                
       
       if s == "":
            return True
       else:
            return False