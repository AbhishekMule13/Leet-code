class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        l = 0
        h = x
        ans = -1

        while l < h:
            mid = l + (h - l) // 2
            if x // mid >= mid:
                ans = mid
                l = mid + 1
            else:
                h = mid

        return ans

            