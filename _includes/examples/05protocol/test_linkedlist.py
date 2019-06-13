import unittest

from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def test_01_repr_empty_list(self):
        llist = LinkedList()
        self.assertEqual('LinkedList[]', str(llist))

    def test_02_append(self):
        llist = LinkedList()
        for i in range(10):
            llist.append(i*2)
        self.assertEqual('LinkedList[0,2,4,6,8,10,12,14,16,18]', str(llist))

    def test_03_len_empty(self):
        llist = LinkedList()
        self.assertEqual(0, len(llist))

    def test_04_len(self):
        sz = 10
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        self.assertEqual(sz, len(llist))
        llist.append('spam')
        self.assertEqual(sz+1, len(llist))

    def test_05_getitem(self):
        size = 10
        llist = LinkedList()
        for i in range(size):
            llist.append(i*2)
        self.assertEqual((4, 6, 10), (llist[2], llist[3], llist[5]))
        with self.assertRaises(TypeError):
            llist['a']
        with self.assertRaises(IndexError):
            llist[size]
        with self.assertRaises(IndexError):
            llist[-1]

    def test_06_contains(self):
        sz = 10
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        self.assertTrue(2 in llist)
        self.assertFalse(42 in llist)

    def test_07_setitem(self):
        sz = 10
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        llist[0] = '-28'
        self.assertEqual("LinkedList['-28',2,4,6,8,10,12,14,16,18]", str(llist))
        llist[sz-1] = 42
        self.assertEqual("LinkedList['-28',2,4,6,8,10,12,14,16,42]", str(llist))
        llist[sz//2] = -sz
        self.assertEqual("LinkedList['-28',2,4,6,8,-10,12,14,16,42]", str(llist))
        self.assertTrue(42 in llist)
        with self.assertRaises(TypeError):
            llist['a'] = 'a'
        with self.assertRaises(IndexError):
            llist[sz] = sz
        with self.assertRaises(IndexError):
            llist[-1] = -1

    def test_08_delitem(self):
        sz = 10
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        del llist[sz-1]
        self.assertEqual("LinkedList[0,2,4,6,8,10,12,14,16]", str(llist))
        del llist[0]
        self.assertEqual("LinkedList[2,4,6,8,10,12,14,16]", str(llist))
        del llist[3]
        self.assertEqual("LinkedList[2,4,6,10,12,14,16]", str(llist))

    def test_09_prepend(self):
        sz = 5
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        for i in range(len(llist),len(llist)+sz):
            llist.prepend(i*3)
        self.assertEqual("LinkedList[27,24,21,18,15,0,2,4,6,8]", str(llist))
        llist = LinkedList()
        for i in range(sz):
            llist.prepend(i*2)
        for i in range(len(llist),len(llist)+sz):
            llist.append(i*3)
        self.assertEqual("LinkedList[8,6,4,2,0,15,18,21,24,27]", str(llist))

    def test_10_insert_empty(self):
        llist = LinkedList()
        llist.insert(0, 'spam')
        self.assertEqual("LinkedList['spam']", str(llist))

    def test_11_insert(self):
        sz = 5
        llist = LinkedList()
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        llist.insert(0, 'spam')
        self.assertEqual("LinkedList['spam',0,2,4,6,8]", str(llist))
        llist.insert(len(llist)-1, 'spam')
        self.assertEqual("LinkedList['spam',0,2,4,6,'spam',8]", str(llist))
        llist.insert(3, 'spam')
        self.assertEqual("LinkedList['spam',0,2,'spam',4,6,'spam',8]", str(llist))
        with self.assertRaises(TypeError):
            llist.insert('a', 'spam')
        with self.assertRaises(IndexError):
            llist.insert(len(llist), 'spam')
        with self.assertRaises(IndexError):
            llist.insert(-1, 'spam')

    def test_12_reverse(self):
        sz = 5
        llist = LinkedList()
        for i in range(sz):
            llist.append(i*2)
        for i in range(len(llist),len(llist)+sz):
            llist.prepend(i*3)
        llist.reverse()
        self.assertEqual("LinkedList[8,6,4,2,0,15,18,21,24,27]", str(llist))

if __name__ == '__main__':
    unittest.main()