from solutions.day_061_linked_list_cycle import ListNode, has_cycle

def test_no_cycle():
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert has_cycle(head) == False

def test_has_cycle():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = head
    assert has_cycle(head) == True

def test_single_node_no_cycle():
    head = ListNode(1)
    assert has_cycle(head) == False