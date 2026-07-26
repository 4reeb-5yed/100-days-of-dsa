from solutions.day_025_merge_sorted_lists import ListNode, merge_two_lists

def test_merge_basic():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(l1, l2)
    vals = []
    curr = merged
    while curr:
        vals.append(curr.val)
        curr = curr.next
    assert vals == [1, 1, 2, 3, 4, 4]

def test_merge_empty():
    assert merge_two_lists(None, ListNode(0)).val == 0

def test_merge_both_empty():
    assert merge_two_lists(None, None) is None
