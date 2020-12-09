# Python Standard Types

## Atomic Types

* `bool` (values: `True`, `False`)
    - Operators: `or`, `and`, `not`
    - Evaluates to `False`:
        - `False`, `None`
        - Numeric zero: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
        - empty sequence or collections:
          `''`, `()`, `[]`, `{}`, `set()`, `range(0)`

* Comparisons
    - `<`       less than, implemented by `__lt__()`
    - `<=`      less than or equal to, implemented by `__le__()`
    - `>`       greater than, implemented by `__gt__()`
    - `>=`      greater than or equal to, implemented by `__ge__()`
    - `==`      equal to, implemented by `__eq__()`,
    - `!=`      not equal to
    - `is`      object identity (`x is y` <=> `id(x) == id(y)`)
    - `is not`  negated object identity

* Membership
    - `in`      contained in, implemented by `__contains__()`
    - `not in`  not contained in

* Numeric types:
    - `int`     integer (ex `0`)
    - `float`   flaoting point real number (ex `0.0`)
    - `complex` complex numbers (ex `1j`)
    - `decimal.Decimal()`   arbitrary precision decimals
    - `fractions.Fraction()` fractions
    - Opertors:
        - `+`, `-`, `*`, `/` (real div), `//` (floor div), `%` (mod),
          `**` (to the power), (unary) `-`, (unary) `+`
        - `abs(x)`          absolute value
        - `c.conjugate()`   complex conjugate
        - `divmod(x, y)`    returns pair of quotient and remainder
        - `pow(x, y)`       x to the power y

* Bitwise operator:
    - `x | y`   bitwise or
    - `x ^ y`   bitwise xor
    - `x & y`   bitwise and
    - `x << n`  left shift by n
    - `x >> n`  right shift by n
    - `~x`      bitwise not (bit inversion)


## Container, Iterator, Generator, Sequence

* Contianer implements `__contains__()`, `__iter__()`, `__len__()`
* Iterator implements `__iter__()` and `__next()__`.
* `container.__iter__()`, `iterator.__iter__()`: returns an
  iterator object.
* Generators: functions that with `yield` (generates an iterator)
* `__iter__()` may be implemented as a generator.
* Sequence types: `list`, `set`, `dict`, `str`.
* `len(s)` returns the length of a sequence.
* `s.copy()` returns a shallow copy of a sequence.
* `s.clear()` clears a mutable sequence

### Lists

* Heterogeneous
* Mutable
* Implemented as Dynamic Arrays
* Operations:
    - `s.append(x)`     O(1) operation to add an element to the end
    - `s.insert(i, x)`  O(n) operation to insert x at index i
    - `s.extend(s1)`    O(n + m) operation to extend the list
    - `s.pop()`         O(1) operation to remove the last element
    - `s.pop(i)`        O(n) pops from i-th index
    - `s.remove(x)`     O(n) removes first occurrence of x
    - `s.index(x)`      O(n) returns the first index for x
    - `s.reverse()`     O(n) reverse in place
    - `s.sort()`        O(n log n) sort in place

### Tuples

* Similar to lists, but immutable.


### Ranges

* Represents immutable sequence of numbers
* Useful in loops
* Usage: `range(stop)`, `range(start, stop)` or `range(start, stop, step)`
    - `start` inclusive, `stop` exclusive.


### Dicts

* Associative array / hashmap.
* Average time of insertion, deletion, and lookup is O(1).
* Keys have to be hashable.
* Mutable
* Main operations:
    - `d.get(k, x)`     O(1) retrieve an item with key k, defaulting to x
    - `d.items()`       view of items (key, value) pairs
    - `d.keys()`        view of keys
    - `d.values()`      view of values stored
    - `d.pop(k, [x])`   O(1) retrieve and delete, default x
    - `d.popitem()`     Remove and return (key, value), in LIFO order
    - `d.update(d1)`    updates from another dict d1


### Sets

* Set object is O(1) add and O(1) membership test
* Items must be hashable
* Mutable
* Main operations:
    - `x in s`          O(1) if x is a member of s
    - `s.isdisjoint(s1)`
    - `s.union(s1)` or `s | s1`
    - `s.intersection(s1)` or `s & s1`
    - `s.issubset(s1)` or `s <= s1`
    - `s < s1` strict subset
    - `s.issuperset(s1)` or `s >= s1`
    - `s > s1` strict superset
    - `s.difference(s1)` or `s - s1`
    - `s.symmetric_difference(s1)` or `s ^ s1`
    - `s.add(x)`        O(1) add an element
    - `s.remove(x)`     O(1) remove an element
    - `s.discard(x)`    O(1) remove an element if present
    - `s.pop()`         O(1) remove and return an arbitrary element

### Strings

* Immutable
* Main operations
    - Most list operations that don't alter the string
    - Formatting: `f-sting`.
    - Concat: `+` (inefficient), try to use `s.join(iterable)`
    - Related to case:
        - `s.lower()`
        - `s.upper()`
        - `s.title()`
        - `s.capitalize()`
        - `s.islower()`
        - `s.isupper()`
        - `s.istitle()`
    - Alignment and modification
        - `s.center(w, [fill])`
        - `s.ljust(w, [fill])`
        - `s.rjust(w, [fill])`
        - `s.strip()`
        - `s.lstrip()`
        - `s.rstrip()`
        - `s.expandtabs(tabsize)`
    - Find and replace
        - `s.index(c)`
        - `s.rindex(c)`
        - `s.find(sub, [start, [end]])`
        - `s.rfind(sub, [start, [end]])`
        - `s.count(sub, [start, [end]])`
        - `s.replace(old, new, [count])`
        - `s.endswith()`
    - Character class
        - `s.isalpha()`
        - `s.isnumeric()`
        - `s.isalnum()`
        - `s.isspace()`
        - `s.isascii()`
        - `s.isdigit()`
        - `s.isdecimal()`
    - Split and join
        - `s.split()`
        - `s.join(A)`


## Useful builtin functions

* `len(s)`              length of a sequence/container
* `id(x)`               identity of an object
* `hash(x)`             hash of a hashable object
* `type(x)`             type of x
* `isinstance(x, t)`    is object x an instance of type t
* `dir(x)`              attributes of an object x
* `sorted(s)`           sorte a sequence
* `reveresed(s)`        reverse a sequence (return iterable)
* `getattr(obj, name, default)`
* `hasattr(obj, name)`
* `map(func, iterable)`
* `filter(bool_func, iterable)`
* `all(bool_iterable)`
* `any(bool_iterable)`
* `exec(s)`
* `eval(s)`
