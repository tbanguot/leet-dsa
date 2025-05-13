class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        integer = 0
        prev_char = s[0]

        for char in s:
            integer += nums[char]
            if nums[prev_char] < nums[char]:
                integer -= 2 * nums[prev_char]
            prev_char = char
        
        return integer
