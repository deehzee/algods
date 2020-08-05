"""
23. Merge k Sorted List
=======================
Merge k sorted linked list and return it as one sorted list.
Analyze and describe its complexity.

Example
-------
Input:
[
    1->4->5,
    1->3->4,
    2->6
]
Output: 1->1->2->3->4->4->5->6

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, a):
        head = tail = None
        for x in a:
            node = cls(x)
            if tail:
                tail.next = node
                tail = node
            else:
                head = tail = node
        return head

    def tolist(self):
        a = []
        this = self
        while this:
            a.append(this.val)
            this = this.next
        return a

    def __repr__(self):
        return repr(f'List({self.tolist()})')


### Solution 1: Using Priority Queue ###

from dataclasses import dataclass, field
import heapq
from typing import Any


@dataclass(order=True)
class HeapItem:
    key: int
    item: Any=field(compare=False)


def merge_lists_pq(lists):
    # Make the queue
    q = []
    for node in lists:
        if node:
            heapq.heappush(q, HeapItem(node.val, node))

    # Pull and push
    head = tail = None
    while q:
        top = heapq.heappop(q)
        nxt = top.item.next
        if nxt:
            heapq.heappush(q, HeapItem(nxt.val, nxt))
        new = ListNode(top.item.val)
        if tail:
            tail.next = new
            tail = new
        else:
            head = tail = new
    return head


### Solution 2: Divide and Conquer ###


def merge_lists_dq(lists):
    if len(lists) == 2:
        return merge(lists[0], lists[1])
    elif len(lists) == 1:
        return lists[0]
    elif len(lists) == 0:
        return

    half = len(lists) // 2
    return merge(merge_lists_dq(lists[:half]),
                 merge_lists_dq(lists[half:]))


def merge(list1, list2):
    head = tail = None
    while list1 and list2:
        if list1.val <= list2.val:
            new = ListNode(list1.val)
            list1 = list1.next
        else:
            new = ListNode(list2.val)
            list2 = list2.next
        if tail:
            tail.next = new
            tail = new
        else:
            head = tail = new
    while list1:
        new = ListNode(list1.val)
        list1 = list1.next
        if tail:
            tail.next = new
            tail = new
        else:
            head = tail = new
    while list2:
        new = ListNode(list2.val)
        list2 = list2.next
        if tail:
            tail.next = new
            tail = new
        else:
            head = tail = new
    return head

