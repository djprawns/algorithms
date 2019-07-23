# https://leetcode.com/problems/longest-substring-without-repeating-characters/solution/

class Solution(object):
    
    def checkIfRepeating(self, map, char):
        if(map.get(char, None)):
            return True
        else:
            return False

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        i = 0
        max = i
        for char in s:
            if self.checkIfRepeating(map, char):
                map = {}
                i=1
                map[char] = 1
            else:
                map[char] = 1
                i+=1
                if i>max:
                    max = i
        return max