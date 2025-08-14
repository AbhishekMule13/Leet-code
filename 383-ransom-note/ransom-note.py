class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        '''
        for ch in ransomNote:
            if ch in magazine:
                magazine=magazine.replace(ch,"",1)
            else :
                return False
        return True            
        '''
        for i in set(ransomNote):
            if(magazine.count(i)< ransomNote.count(i)):
                return False
        return True        