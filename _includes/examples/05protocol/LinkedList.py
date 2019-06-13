from dataclasses import dataclass
from typing import Any
from collections.abc import MutableSequence

@dataclass
class Node:
    data : Any
    next : Any

class LListIterator:
    def __init__(self, llist):
        self._iter_pos = llist.head

    def __iter__(self):
        return self

    def __next__(self):
        if self._iter_pos == None:
            raise StopIteration
        else:
            cur = self._iter_pos
            self._iter_pos = cur.next
            return cur.data

class LinkedList(MutableSequence):
    def __init__(self):
        self._num_nodes = 0
        self.head = None
        self.tail = None

    def append(self, value):
        e = Node(value, next=None)
        if self.head is None:
            self.head = e
        else:
            self.tail.next = e
        self.tail = e
        self._num_nodes += 1

    def prepend(self, value):
        e = Node(value, next=self.head)
        self.head = e
        if self.tail is None:
            self.tail = e
        self._num_nodes += 1

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def insert(self, index, value):
        if index == 0 and self._num_nodes == 0:
            self.prepend(value)
        elif self._index_ok(index):
            return self._ins(index, value)

    def __len__(self):
        return self._num_nodes

    def __repr__(self):
        contents_str = ','.join([f'{x!r}' for x in self])
        return f'{self.__class__.__qualname__}[{contents_str}]'

    def __getitem__(self, i):
        if self._index_ok(i):
            return self._get(i)

    def __setitem__(self, i, x):
        if self._index_ok(i):
            return self._set(i, x)

    def __delitem__(self, i):
        if self._index_ok(i):
            return self._del(i)

    def __contains__(self, x):
        for val in self:
            if val == x:
                return True
        return False

    def __iter__(self):
        return LListIterator(self)

    # prevent reverse itertion
    __reversed__ = None

    def _index_ok(self, i):
        if isinstance(i,int):
            if 0 <= i < self._num_nodes:
                return True
            else:
                raise IndexError
        else:
            raise TypeError(f'{self.__class__.__qualname__} index {i!r} must be int')

    def _get(self, i):
        pos = 0
        ret = self.head
        while (pos < i):
            ret = ret.next
            pos += 1
        return ret.data

    def _set(self, i, x):
        pos = 0
        c = self.head
        while (pos < i):
            c = c.next
            pos += 1
        c.data = x

    def _del(self, i):
        if i == 0:
            cur_head = self.head
            self.head = cur_head.next
            cur_head.next = None
        else:
            p = self.head
            c = p.next
            pos = 1
            while pos < i:
                p = c
                c = c.next
                pos += 1
            p.next = c.next
            c.next = None
            if c == self.tail:
                self.tail = p
        self._num_nodes -= 1

    def _ins(self, i, x):
        if i == 0:
            e = Node(x, next=self.head)
            self.head = e
        else:            
            p = self.head
            c = p.next
            pos = 1
            while pos < i:
                p = c
                c = c.next
                pos += 1
            e = Node(x, next=c)
            p.next = e
        self._num_nodes += 1
