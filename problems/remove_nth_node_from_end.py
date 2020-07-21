def remove_nth_node_from_end(head, n):
    counter = 1
    first = head
    second = head

    while counter <= n:
        second = second.next
        counter += 1
        if second is None:
            head = None
            return head

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return head

    while second.next is not None:
        second = second.next
        first = first.next

    first.next = first.next.next
    return head
