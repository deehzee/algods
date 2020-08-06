'''
199. Binary Tree Right Side View
================================

Given a binary tree, imagine yourself standing on the right side
of it, return the values of the nodes you can see ordered from top
to bottom.

'''

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isleaf(self):
        return self.left is None and self.right is None

    @classmethod
    def from_list(cls, a):
        nodes = [TreeNode(x) if x is not None else None for x in a]
        for i in range(1, len(a)):
            if i % 2:
                nodes[(i - 1) // 2].left = nodes[i]
            else:
                nodes[(i - 1) // 2].right = nodes[i]
        return nodes[0] if nodes else None

    def to_list(self):
        a = []
        q = deque([self])
        while q:
            node = q.popleft()
            a.append(node.val)
            q.append(node.left)
            q.append(node.right)
        i = -1
        while a[i] is None:
            i -= 1
        return a[:(i + 1)]


def list2bintree(a):
    nodes = [TreeNode(x) if x is not None else None for x in a]
    for i in range(1, len(a)):
        if i % 2:
            nodes[(i - 1) // 2].left = nodes[i]
        else:
            nodes[(i - 1) // 2].right = nodes[i]
    return nodes[0] if nodes else None


def bintree2list(tree):
    a = []
    if not tree:
        return a
    q = deque([tree])
    while q:
        node = q.popleft()
        if node:
            a.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            a.append(None)
    i = -1
    while a[i] is None:
        i -= 1
    return a[:(i + 1)]


def right_side_view1(tree):
    a = []
    if not tree:
        return a
    # store (node, level) in the queue
    q = deque([(tree, 0)])
    last = -1  # last level
    while q:
        node, level = q.popleft()
        if level != last:
            last = level
            a.append(node.val)
        if node.right:
            q.append((node.right, level + 1))
        if node.left:
            q.append((node.left, level + 1))
    return a


def right_side_view2(a):
    view = []
    start, end = 0, 1
    while start < len(a):
        for i in reversed(range(start, min(end, len(a)))):
            if a[i] is None:
                continue
            view.append(a[i])
            break
        start, end = end, 2 * end + 1
    return view


if __name__ == '__main__':
    import doctest
    doctest.testmod()

