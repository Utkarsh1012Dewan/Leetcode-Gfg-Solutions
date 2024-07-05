# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        index = 2
        track = head.next
        arr = []

        if not track.next:
            return [-1,-1]
        
        while track.next:
            if (track.val > head.val and track.val > track.next.val) or (track.val < head.val and track.val < track.next.val):
                arr.append(index)
            track = track.next
            head = head.next
            index +=1
        

        if len(arr) < 2:
            return [-1,-1]
        elif len(arr) == 2:
            return [arr[-1]-arr[0],arr[-1]-arr[0]]

        minVal = float("inf")
        for i in range(1,len(arr)):
            minVal = min(arr[i]-arr[i-1],minVal)
        return [minVal, arr[-1]-arr[0]]

        