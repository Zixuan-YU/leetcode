class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        vsum = 0
        prev = 0
        v = 0
        for i in s[::-1]:
            prev = v
            
            v = dict.get(i)
            if prev > v:
                vsum -= v
            else:
                vsum += v
        
        return vsum
                
