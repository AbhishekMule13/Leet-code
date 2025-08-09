class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, 2)
        y = int(b, 2)
        
       
        total = x + y
        
        
        return bin(total)[2:]



sol = Solution()
print(sol.addBinary("11", "1"))       
print(sol.addBinary("1010", "1011")) 