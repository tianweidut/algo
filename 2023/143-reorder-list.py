    def reorderList(self, head) -> None:
        if head is None or head.next is None or head.next.next is None:
            return

        prev_tail = head
        while prev_tail.next.next is not None:
            prev_tail = prev_tail.next

        tail = prev_tail.next
        prev_tail.next = None
        tail.next = head.next
        head.next = tail
        self.reorderList(tail.next)
