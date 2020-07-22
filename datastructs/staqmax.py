from collections import deque, namedtuple

Node = namedtuple('Node', ['key', 'max'])


class StackMax:
    def __init__(self):
        self.__store = deque()

    def push(self, x):
        if self.empty():
            m = x
        else:
            m = max(x, self.__store[-1].key)
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

