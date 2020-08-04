# python3
from collections import deque, namedtuple
import sys

## Data Structures ##


Node = namedtuple('Node', ['key', 'max'])


class StackMax:
    def __init__(self):
        self.__store = deque()

    def push(self, x):
        if self.empty():
            m = x
        else:
            m = max(x, self.__store[-1].max)
        self.__store.append(Node(x, m))

    def pop(self):
        assert not self.empty(), 'stack is emtpy'
        return self.__store.pop().key

    def popmax(self):
        assert not self.empty(), 'stack is emtpy'
        return self.__store.pop().max

    def top(self):
        assert not self.empty(), 'stack is emtpy'
        return self.__store[-1].key

    def max(self):
        assert not self.empty(), 'stack is emtpy'
        return self.__store[-1].max

    def empty(self):
        return len(self.__store) == 0

    def __repr__(self):
        return repr(self.__store)

    def __len__(self):
        return len(self.__store)


class QueueMax:
    def __init__(self):
        self.__head = StackMax()
        self.__tail = StackMax()

    def enqueue(self, x):
        self.__tail.push(x)
        pass

    def __rebalance(self):
        if self.__head.empty():
            while not self.__tail.empty():
                self.__head.push(self.__tail.pop())

    def dequeue(self):
        assert not self.empty(), 'queue is empty'
        self.__rebalance()
        return self.__head.pop()

    def dequeuemax(self):
        assert not self.empty(), 'queue is empty'
        self.__rebalance()
        return self.__head.popmax()

    def head(self):
        assert not self.empty(), 'queue is empty'
        return self.__head.top()

    def headmax(self):
        assert not self.empty(), 'queue is empty'
        return self.__head.max()

    def tail(self):
        assert not self.empty(), 'queue is empty'
        return self.__tail.top()

    def tailmax(self):
        assert not self.empty(), 'queue is empty'
        return self.__tail.max()

    def max(self):
        assert not self.empty(), 'queue is empty'
        if self.__head.empty():
            return self.__tail.max()
        if self.__tail.empty():
            return self.__head.max()
        return max(self.__head.max(), self.__tail.max())

    def empty(self):
        return len(self.__head) + len(self.__tail) == 0

    def __repr__(self):
        return (
            'head: ' + repr(self.__head) +
            '\ntail: '  + repr(self.__tail)
        )

    def __len__(self):
        return len(self.__head) + len(self.__tail)


class SlidingWindowMax:
    def __init__(self, window):
        self.__store = QueueMax()
        self.window = window
        self.size = 0

    def process(self, x):
        if self.size == self.window:
            self.__store.dequeue()
            self.size -= 1
        self.__store.enqueue(x)
        self.size += 1
        if self.size == self.window:
            return self.__store.max()

    def __repr__(self):
        return repr(self.__store)

    def __len__(self):
        return len(self.__store)


## End Data Structures ##`


def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


def max_sliding_window_stacks(a, m):
    # Implementation using two stacks
    maxs = []
    slwin = SlidingWindowMax(window=m)
    for x in a:
        m = slwin.process(x)
        if m is not None:
            maxs.append(m)
    return maxs


def get_input(f):
    n = int(f.readline())
    a = list(map(int, f.readline().split()))
    m = int(f.readline())
    assert m <= len(a)
    return n, a, m


def main():
    n, a, m = get_input(sys.stdin)
    print(*max_sliding_window_stacks(a, m))


if __name__ == '__main__':
    main()
