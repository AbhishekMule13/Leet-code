class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prifix = strs[0]

        for word in strs[1:] :
            while not word.startswith(prifix):
                prifix=prifix[:-1]
                if prifix=="":
                    return "" 
        return prifix         

        
        