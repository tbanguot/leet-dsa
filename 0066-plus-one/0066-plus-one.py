class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        arr = []
        n = len(digits)
        for _ in range(n):
            d = digits.pop() + plus
            arr.append(d % 10)
            plus = d // 10
        
        if plus:
            arr.append(plus)

        n = len(arr)
        for _ in range(n):
            digits.append(arr.pop())
        
        return digits
            

        