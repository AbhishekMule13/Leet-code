class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign= -1 if x<0 else 1   
        str_x = str(abs(x))
        reversed_str = str_x[::-1]
        reversed_num = sign * int(reversed_str)
        if reversed_num < -2**31 or reversed_num > 2**31-1:
            return 0
        return reversed_num
        
        