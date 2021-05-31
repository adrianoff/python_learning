class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        rev = 0
        ax = x
        while ax != 0:
            pop = ax % 10
            ax = int(ax/10)
            rev = rev * 10 + pop

        if rev == x:
            return True

        return False

a = Solution().isPalindrome(121)