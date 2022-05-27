"""
@author: rochak.bhalla@ymail.com
"Beginner to Leetcode, you might peek in to this soultion for better understanding ;)"

This soultion has run in 17ms which is faster than the 90% online submissions, as per the leetcode data.

The solution checks if the first element is roman number or not, if yes then it checks, whether its not a last elemnt of string.
If not, then it checks for the immedidate number if that comes in the below crieteria:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900 
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val=0 
        i=0
        while(i < len(s)):
            if s[i] == "I":
                if i== len(s)-1:
                    val = val +1
                    break
                else:
                    rt = self.retvalI(s[i], s[i+1])
                    if rt == 1:
                        val = val+rt
                        i=i+1
                    else:
                        val = val+rt
                        i=i+2
            
            elif s[i] == "V":
                if i== len(s)-1:
                    val = val + 5
                    break
                else:
                    val = val + 5
                    i=i+1
            
            elif s[i] == "X":
                if i== len(s)-1:
                    val = val +10
                    break
                else:
                    rt = self.retvalX(s[i], s[i+1])
                    if rt == 10:
                        val = val+rt
                        i=i+1
                    else:
                        val = val+rt
                        i=i+2
            
            elif s[i] == "L":
                if i== len(s)-1:
                    val = val +50
                    break
                else:
                    val = val +50
                    i=i+1
            
            elif s[i] == "C":
                if i== len(s)-1:
                    val = val +100
                    break
                else:
                    rt = self.retvalC(s[i], s[i+1])
                    if rt == 100:
                        val = val+rt
                        i=i+1
                    else:
                        val = val+rt
                        i=i+2
            
            elif s[i] == "D":
                if i== len(s)-1:
                    val = val + 500
                    break
                else:
                    val = val + 500
                    i=i+1
            
            elif s[i] == "M":
                if i== len(s)-1:
                    val = val + 1000
                    break
                else:
                    val = val + 1000
                    i=i+1    
        return val
    
    def retvalI(self, firstindx, secondindx):
        if firstindx == "I" and secondindx == "V":
            return int(4)
        elif firstindx == "I" and secondindx == "X":
            return int(9)
        else:
            return int(1)
    def retvalX(self, firstindx, secondindx):
        if firstindx == "X" and secondindx == "L":
            return int(40)
        elif firstindx == "X" and secondindx == "C":
            return int(90)
        else:
            return int(10)
    def retvalC(self, firstindx, secondindx):
        if firstindx == "C" and secondindx == "D":
            return int(400)
        elif firstindx == "C" and secondindx == "M":
            return int(900)
        else:
            return int(100)

    
s = Solution()
s.romanToInt("MCMXCIV")
