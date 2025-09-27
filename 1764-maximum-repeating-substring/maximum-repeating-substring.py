class Solution(object):
    def maxRepeating(self, sequence, word):
        """
        :type sequence: str
        :type word: str
        :rtype: int
        """
        k=0
        repeted_word = word

        while repeted_word in sequence :
            k+=1
            repeted_word+=word
        return k    
             

        