'''Stacks and Queues with Max'''

from collections import deque, namedtuple
from random import randint

Node = namedtuple('Node', ['value', 'max'])


class StackMax:
    '''Stack with maximum.'''

    def __init__(self):
        self.__store = deque()

    def push(self, x):
        if self.empty():
            m = x
        else:
            m = max(x, self.__store[-1].max)
        self.__store.append(Node(x, m))

    def pop(self):
        assert not self.empty(), 'stack is empty'
        return self.__store.pop().value

    def top(self):
        assert not self.empty(), 'stack is empty'
        return self.__store[-1].value

    def max(self):
        assert not self.empty(), 'stack is empty'
        return self.__store[-1].max

    def empty(self):
        return len(self.__store) == 0

    def __repr__(self):
        return f'StackMax({list(self.__store)})'

    def __len__(self):
        return len(self.__store)


class QueueMax:
    '''Queue with maximum, implemented with two stacks.'''

    def __init__(self):
        self.__head = StackMax()
        self.__tail = StackMax()

    def enqueue(self, x):
        self.__tail.push(x)

    def __rebalance(self):
        while not self.__tail.empty():
            self.__head.push(self.__tail.pop())

    def dequeue(self):
        assert not self.empty(), 'queue is empty'
        if self.__head.empty():
            self.__rebalance()
        return self.__head.pop()

    def max(self):
        assert not self.empty(), 'queue is empty'
        if self.__head.empty():
            return self.__tail.max()
        if self.__tail.empty():
            return self.__head.max()
        return max(self.__head.max(), self.__tail.max())

    def empty(self):
        return len(self.__head) + len(self.__tail) == 0

    def __len__(self):
        return len(self.__head) + len(self.__tail)

    def __repr__(self):
        return f'QueueMax(head={repr(self.__head)}, tail={repr(self.__tail)})'


class MaxQueue:
    '''Maximum queue (does not store all the numbers), with deque.'''

    def __init__(self):
        self.__store = deque()

    def enqueue(self, x):
        while not self.empty():
            if self.__store[-1] < x:
                self.__store.pop()
            else:
                break
        self.__store.append(x)

    def dequeue(self):
        assert not self.empty(), 'queue is empty'
        return self.__store.popleft()

    def max(self):
        assert not self.empty(), 'queue is empty'
        return self.__store[0]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self.__store)

    def __repr__(self):
        return f'MaxQueue({list(self.__store)})'


def test_stack_max(maxlen=5, maxnum=10, seed=42):
    try:
        n = 0
        while True:
            n += 1
            a = [randint(1, maxnum) for _ in range(randint(1, maxlen))]
            x = [max(a[:i + 1]) for i in range(len(a))]
            s = StackMax()
            y = []
            for _ in a:
                s.push(_)
                y.append(s.max())
            if x != y:
                print(f'Failed test#{n}\na={a}\nx={x}\ny={y}')
                break
            z = []
            while not s.empty():
                z.append(s.max())
                s.pop()
            x = list(reversed(x))
            if x != z:
                print(f'Failed test#{n}\na={a}\nx={x}\nz={z}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def test_queue_max(maxlen=10, maxnum=10, maxwin=10, seed=42):
    try:
        n = 0
        while True:
            n += 1
            a = [randint(1, maxnum) for _ in range(randint(1, maxlen))]
            window = randint(1, min(maxwin, len(a)))
            if len(a) < window:
                continue
            x = [max(a[i: i + window]) for i in range(len(a) - window + 1)]
            y = []
            q = QueueMax()
            for i in range(window):
                q.enqueue(a[i])
            for i in range(window, len(a)):
                y.append(q.max())
                q.dequeue()
                q.enqueue(a[i])
            y.append(q.max())
            if x != y:
                print(f'Failed test#{n}\na={a}, window={window}\nx={x}\ny={y}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


def test_max_queue(maxlen=10, maxnum=10, maxwin=10, seed=42):
    try:
        n = 0
        while True:
            n += 1
            a = [randint(1, maxnum) for _ in range(randint(1, maxlen))]
            window = randint(1, min(maxwin, len(a)))
            if len(a) < window:
                continue
            x = [max(a[i: i + window]) for i in range(len(a) - window + 1)]
            y = []
            q = MaxQueue()
            for i in range(window):
                q.enqueue(a[i])
            for i in range(window, len(a)):
                y.append(q.max())
                q.dequeue()
                q.enqueue(a[i])
            y.append(q.max())
            if x != y:
                print(f'Failed test#{n}\na={a}, window={window}\nx={x}\ny={y}')
                break
    except KeyboardInterrupt:
        print(f'Passed: {n}')


if __name__ == '__main__':
    test_queue_max()

