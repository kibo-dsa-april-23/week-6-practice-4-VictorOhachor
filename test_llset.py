import unittest
from llset import LLSet

class TestLLSet(unittest.TestCase):
    def setUp(self):
        self.llset = LLSet()

    def test_insert(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)

        items = self.llset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items

    def test_insert_dup(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)
        assert not self.llset.insert(3)

    def test_size(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)

        assert self.llset.size() == 3

    def test_contains(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)

        assert self.llset.contains(2)

    def test_delete_present(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)

        assert self.llset.delete(2)

        items = self.llset.to_list()
        assert len(items) == 2
        assert 1 in items and 3 in items

    def test_delete_not_present(self):
        assert self.llset.insert(1)
        assert self.llset.insert(2)
        assert self.llset.insert(3)

        assert not self.llset.delete(5)

        items = self.llset.to_list()
        assert len(items) == 3
        assert 1 in items and 2 in items and 3 in items
