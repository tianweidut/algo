# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda a, b: a.val < b.val

class Solution:
    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import sys
        head = sentry_node = ListNode()
        
        while len(lists) > 0:
            lists = [l for l in lists if l]

            min_val = sys.maxsize
            min_idx = -1
            for idx, val in enumerate(lists):
                if lists[idx].val < min_val:
                    min_val = lists[idx].val
                    min_idx = idx
            if min_idx == -1:
                break
            
            head.next = lists[min_idx]
            lists[min_idx] = lists[min_idx].next
            head = head.next

        return sentry_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import sys
        import heapq

        head = sentry_node = ListNode()

        lists = [l for l in lists if l]
        heapq.heapify(lists)

        while len(lists) > 0:
            min_node = heapq.heappop(lists)

            head.next = min_node
            head = head.next

            if min_node.next:
                heapq.heappush(lists, min_node.next)
        
        return sentry_node.next
