---
title: Protocols
---

# Protocols

--

## Definition
- A protocol defines a set of methods an object must support in order to implement it
- Python has multiple protocols that user code can tap into
- Most common protocols are `Collection` and `Iterator`
  - See the module <span style="color:indianred">`collections.abc`</span> in the Standard Library 

--

## Collection
- A sized iterable container class
- Special methods for `Collection`
  - <span style="color:indianred">`__iter__`</span>, <span style="color:indianred">`__contains__`</span>, and <span style="color:indianred">`__len__`</span>

```python
>>> from LinkedList import LinkedList
>>> llist = LinkedList()
>>> for i in range(10): llist.append(i)
>>> sum(llist)
45
>>> 5 in llist
True
>>> len(llist)
10
```

--

## Implementation
- <span style="color:indianred">`__iter__`</span>

```python
    def __iter__(self):
        return LListIterator(self)
```
- <span style="color:indianred">`__contains__`</span>

```python
    def __contains__(self, item):
        for val in self:
            if val == item:
                return True
        return False
```
- <span style="color:indianred">`__len__`</span>

```python
    def __len__(self):
        return self._num_nodes
```

--

## Sequence
- Methods for `Sequence` containers
  - Methods from `Collection` plus <span style="color:indianred">`__getitem__`</span> (<span style="color:indianred">`[]`</span> operator)
  - Can also include <span style="color:indianred">`__reversed__`</span>, <span style="color:indianred">`index`</span>, <span style="color:indianred">`count`</span>
- Additional methods for `MutableSequence`
  - <span style="color:indianred">`__setitem__`</span>, <span style="color:indianred">`__delitem__`</span>
  - Can include several more methods (e.g., <span style="color:indianred">`append`</span>)
- Reminder: when emulating a built-in type, generally should only implement the methods that you need

--

## Mapping
- Methods for `Mapping` containers
  - Methods from `Collection` plus <span style="color:indianred">`__getitem__`</span>, <span style="color:indianred">`__iter__`</span>, <span style="color:indianred">`__len__`</span>
  - Can also include <span style="color:indianred">`__contains__`</span>, <span style="color:indianred">`keys`</span>, <span style="color:indianred">`items`</span>, <span style="color:indianred">`values`</span>, <span style="color:indianred">`get`</span>, <span style="color:indianred">`__eq__`</span>, <span style="color:indianred">`__ne__`</span>
- Additional methods for `MutableMapping`
  - <span style="color:indianred">`__setitem__`</span>, <span style="color:indianred">`__delitem__`</span>
  - Can include several more methods (e.g., <span style="color:indianred">`clear`</span>)

--

## Iterator
- The object that **iterates** over an **iterable** (e.g., a sequence)
- An **iterable** needs to implement
  - <span style="color:indianred">`__iter__`</span> which returns an **iterator**
- An **iterator** needs to implement
  - <span style="color:indianred">`__iter__`</span> which returns <span style="color:indianred">`self`</span>
  - <span style="color:indianred">`__next__`</span>
    - Returns the next item from the container
    - Raise <span style="color:indianred">`StopIteration`</span> when there are no further items in the container

--

## Implementation
- <span style="color:indianred">`__iter__`</span>

```python
    def __iter__(self):
        return self
```
- <span style="color:indianred">`__next__`</span>

```python
    def __next__(self):
        if self._iter_pos == None:
            raise StopIteration
        else:
            cur = self._iter_pos
            self._iter_pos = cur.next
            return cur.data
```

--

## Example Of Iterator Behavior
```python
>>> from LinkedList import LinkedList
>>> llist = LinkedList()
>>> for i in range(2): llist.append(chr(ord('a')+i))
>>> i = iter(llist)
>>> next(i)
'a'
>>> next(i)
'b'
>>> next(i)
Traceback (most recent call last):
  ...<snip>...
StopIteration
>>> for i in range(len(llist)): print(f'Item {i} is {llist[i]}')
Item 0 is a
Item 1 is b
```
