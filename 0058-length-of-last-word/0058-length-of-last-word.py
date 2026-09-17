class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       lastword = s.split()
       return len(lastword[-1])