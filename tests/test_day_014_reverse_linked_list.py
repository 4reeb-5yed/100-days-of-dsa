from solutions.day_014_reverse_linked_list import ListNode, reverse_list

def test_reverse_basic():
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reversed_head = reverse_list(head)
    assert reversed_head.val == 5

def test_reverse_two_elements():
    head = ListNode(1, ListNode(2))
    reversed_head = reverse_list(head)
    assert reversed_head.val == 2
    assert reversed_head.next.val == 1

def test_reverse_single():
    head = ListNode(1)
    reversed_head = reverse_list(head)
    assert reversed_head.val == 1
    assert reversed_head.next is None
