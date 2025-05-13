class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        majorElem = None
        majorVal = 0
        for key, val in d.items():
            if val > len(nums) // 2:
                return key
        