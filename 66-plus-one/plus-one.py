class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        string_digits = map(str, digits)         
        joined_string = "".join(string_digits)  
        num = int(joined_string)                
        num += 1      
                                  
        num_str = str(num)                   
        result = list(map(int, num_str))        

        return result

        