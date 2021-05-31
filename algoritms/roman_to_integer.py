class Solution(object):
    def romanToInt(self, s):

        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        res = 0
        for i in range(0, len(s)-1):
            if map[s[i]] < map[s[i+1]]:
                res -= map[s[i]]
            else:
                res += map[s[i]]
        res += map[s[i+1]]

        return res

s = 'LVIII'
res = Solution().romanToInt(s)
print(res)

