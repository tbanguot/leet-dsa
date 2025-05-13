# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        sizeA = 0
        currA = headA
        while currA:
            sizeA += 1
            currA = currA.next
        
        sizeB = 0
        currB = headB
        while currB:
            sizeB += 1
            currB = currB.next
        
        diff = sizeA - sizeB if (sizeA - sizeB) >= 0 else sizeB - sizeA
        
        if sizeA > sizeB:
            for _ in range(diff):
                headA = headA.next
        elif sizeB > sizeA:
            for _ in range(diff):
                headB = headB.next
            
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        return None
            