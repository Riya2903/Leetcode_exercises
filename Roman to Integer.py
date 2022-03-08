class Solution:
    def romanToInt(self, s: str) -> int:
        special_numerals = {"IV": " 4 ", "IX": " 9 ", "XL": " 40 ", "XC": " 90 ", "CD": " 400 ", "CM": " 900 "}
        numerals = {"I": " 1 ", "V": " 5 ", "X": " 10 ", "L": " 50 ", "C": " 100 ", "D": " 500 ", "M": " 1000 "}
        for key1,value in special_numerals.items():
            if key1 in s:
                s = s.replace(key1,value)
        for key2,value  in numerals.items() :
            if key2 in s:
                s = s.replace(key2,value)
        st = 0           
        for n in s.split():
            st =st + int(n)
        return st