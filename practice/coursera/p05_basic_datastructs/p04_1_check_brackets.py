# python3

from collections import deque
from collections import namedtuple
from pathlib import Path

Bracket = namedtuple("Bracket", ["char", "position"])

#### Implementation 1: Stack using `deque` ####

class Stack1:
    def __init__(self):
        self.store = deque()

    def push(self, x):
        self.store.append(x)

    def pop(self):
        return self.store.pop()

    def empty(self):
        return len(self.store) == 0


#### Implementation 2: Stack using Linked list ####

StackNode = namedtuple('StackNode', 'key nxt')


class Stack2:

    def __init__(self):
        self.top = None

    def push(self, x):
        self.top = StackNode(x, self.top)

    def pop(self):
        if self.empty():
            raise IndexError('pop from an empty stack')
        x = self.top.key
        self.top = self.top.nxt
        return x

    def empty(self):
        return self.top is None


#### End of data struct implementations ####

Stack = Stack2


def matches(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = Stack()
    for i, c in enumerate(text):
        if c in "([{":
            stack.push(Bracket(c, i + 1))
        elif c in ")]}":
            if stack.empty() or not matches(stack.pop().char, c):
                return i + 1
    if not stack.empty():
        return stack.pop().position
    return 0


def tests():
    tests_root = Path('tests1')
    n_tests = 54
    for i in range(n_tests):
        input_file = tests_root / f'{(i + 1):02d}'
        output_file = tests_root / f'{(i + 1):02d}.a'
        with input_file.open() as f:
            test_input = f.read()
        with output_file.open() as f:
            test_output = f.read()
        mismatch = find_mismatch(test_input)
        if mismatch == 0:
            output = 'Success\n'
        else:
            output = f'{mismatch}\n'
        if output != test_output:
            print(f'Failed test#{i + 1}')
            print(f'Expected Output: {test_output}')
            print(f'     Got Output: {output}')


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == 0:
        print('Success')
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
    # tests()

