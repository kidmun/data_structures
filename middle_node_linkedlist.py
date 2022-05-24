def get_middle_node():

    faster_pointer = head
    slower_pointer = head
    while faster_pointer.next and faster_pointer.next.next:
        faster_pointer = faster_pointer.next.next
        slower_pointer = slower_pointer.next

    return slower_pointer
        

