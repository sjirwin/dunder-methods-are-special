from dataclasses import dataclass
from typing import Any

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

class LinkedList:
    def __init__(self):
        self._num_nodes = 0
        self.head = None
        self.tail = None

    def append(self, x):
        e = Node(x, next=None)
        if self.head is None:
            self.head = e
        else:
            self.tail.next = e
        self.tail = e
        self._num_nodes += 1

    def prepend(self, x):
        e = Node(x, next=self.head)
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

    def __iter__(self):
        return LListIterator(self)

    def _get(self, index):
        pos = 0
        ret = self.head
        while (pos < index) and (ret is not None):
            ret = ret.next
            pos += 1
        return ret.data

    def __getitem__(self, index):
        if isinstance(index,int):
            if 0 <= index < self._num_nodes:
                return self._get(index)
            else:
                raise IndexError
        else:
            raise TypeError(f'{self.__class__.__qualname__}.__getitem__ index({index!r}) must be int')

    def __contains__(self, item):
        for val in self:
            if val == item:
                return True
        return False

    def __len__(self):
        return self._num_nodes

    def __repr__(self):
        return ','.join([str(val) for val in self])

def main():
    llist = LinkedList()
    for i in range(10):
        llist.append(i)
    print(f'llist = {llist!r}')

    for i in range(len(llist)):
        print(llist[i])

    print(f'llist[2] = {llist[2]!r}')

    print(f' 5 is in llist: {5 in llist}')
    print(f'42 is in llist: {42 in llist}')

    for i in range(10,20):
        llist.prepend(i)
    print(f'llist = {llist!r}')

    llist.reverse()
    print(f'reversed llist = {llist!r}')

if __name__ == '__main__':
    main()