class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone={
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }    

        res = [""]
        for digit  in digits:
            new_list = []
            for i in res:
                for j in phone[digit]:
                    new_list.append(i+j)
            res=new_list       
        return res
