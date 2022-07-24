class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #s1 = s.rstrip()
        n = len(s.split())
        return len(s.split()[n-1].rstrip())
