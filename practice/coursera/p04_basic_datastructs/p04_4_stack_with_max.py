#python3
from collections import namedtuple
import sys

StackElt = namedtuple('StackElt', ['key', 'max'])


class StackWithMax():
    def __init__(self):
        self.__stack = []

    def push(self, a):
        if self.empty():
            m = a
        else:
            m = max(a, self.__stack[-1].max)
        self.__stack.append(StackElt(a, m))

    def pop(self):
        if self.empty():
            raise IndexError('pop from an empty stack')
        self.__stack.pop()

    def max(self):
        if self.empty():
            raise IndexError('pop from an empty stack')
        return self.__stack[-1].max

    def empty(self):
        return len(self.__stack) == 0

    def print(self):
        print(self.__stack)


def main():
    stack = StackWithMax()
    n = int(input())
    for _ in range(n):
        com = input().split()
        if com[0] == "push":
            stack.push(int(com[1]))
        elif com[0] == "pop":
            stack.pop()
        elif com[0] == "max":
            print(stack.max())
        else:
            assert(0)


if __name__ == '__main__':
    main()

