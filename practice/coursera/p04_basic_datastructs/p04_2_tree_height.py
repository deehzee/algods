# python3

from collections import namedtuple
import sys
import threading

Tree = namedtuple('Tree', 'key children')


def build_tree(parents):
    nodes = [Tree(i, []) for i in range(len(parents))]
    for i, parent in enumerate(parents):
        if parent == -1:
            root = nodes[i]
            continue
        nodes[parent].children.append(nodes[i])
    return root


def height(tree):
    if len(tree.children) == 0:
        return 1
    return 1 + max(height(child) for child in tree.children)


def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = build_tree(parents)
    # print(compute_height(n, parents))
    print(height(tree))


if __name__ == '__main__':
    # In Python, the default limit on recursion depth is rather low,
    # so raise it here for this problem. Note that to take advantage
    # of bigger stack, we have to launch the computation in a new thread.
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
