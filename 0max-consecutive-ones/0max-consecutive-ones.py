class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max = 0
        
        for num in nums:
            if num:
                curr_max += 1
            else:
                if curr_max > prev_max:
                    prev_max = curr_max
                curr_max = 0
        
        return prev_max if prev_max > curr_max else curr_max
            
        