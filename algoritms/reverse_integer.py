class Solution(object):
    def reverse(self, x):
        res = 0
        ax = abs(x)
        while ax != 0:
            pop = ax % 10
            ax = int(ax/10)
            res = res * 10 + pop

        if (x < 0):
            res *= -1

        return res

b = -123 % -10
a = Solution().reverse(-123)