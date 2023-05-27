# Linked List Set

In this practice, you will implement the set ADT using a linked list. In one of your assignments, you implemented a set using a list, a sorted list, and a file. Now, you will implement the same ADT using a linked list.

## Starter Code

In `llset.py`, you are given the partial implementation of the `LLSet` object, which is a set based on a linked list. The linked list will be composed of nodes from the nested `Node` class.

The `LLSet` class has stub implementations of the following methods:

- `insert(item)`: insert an item into the set; returns `True` on successful insertion, `False` otherwise (for example, if the item is already in the set
- `contains(item)`: returns whether the set contains the item
- `delete(item)`: delete an item from the set; returns `True` on successful deletion, `False` otherwise (for example, if the item was not in the set)
- `size()`: returns the number of elements in the set
- `to_list()`: returns the set as a Python list

## Steps to Complete

Implement the methods of the `LLSet` class in any order that you wish. While you do so, remember that a set has the following properties:

- Each element in the set is unique; there can't be any duplicates
- A set is unordered; there is no notion of "position i" in a set

Your `LLSet` class must respect these properties. You should implement your methods as efficiently as possible. And of course, you should use a linked list!

You may find it useful to refer back to the week's lessons to see how to insert nodes into a list, traverse a list, delete a node from a list, etc.

## Testing

We have provided all of the unit tests you should need to test for basic functional correctness of the `LLSet` class in `test_llset.py`. If you wish, you are welcome to add more unit tests.
