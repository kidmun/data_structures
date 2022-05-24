# O(N) inplace solution
def reverse_slinked_list():
    current = head
    prev_node = None
    next_node = None

    while current:
        next_node = current.next
        current.next = prev_node
        prev_node = current
        current = next_node

    head = prev_node
