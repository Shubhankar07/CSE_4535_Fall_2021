# -*- coding: utf-8 -*-
"""linkedlist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYONqjT4ZY3hAEsn2PnaeLdhgCyIKj5F
"""

# -*- coding: utf-8 -*-
"""linkedlist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VYONqjT4ZY3hAEsn2PnaeLdhgCyIKj5F
"""

import math


class Node:

    def __init__(self, value=None, next=None, skip=None, tfidf=None):
        """ Class to define the structure of each node in a linked list (postings list).
            Value: document id, Next: Pointer to the next node
            Add more parameters if needed.
            Hint: You may want to define skip pointers & appropriate score calculation here"""
        self.value = value
        self.next = next
        self.skip = skip
        self.tfidf = tfidf


class LinkedList:
    """ Class to define a linked list (postings list). Each element in the linked list is of the type 'Node'
        Each term in the inverted index has an associated linked list object.
        Feel free to add additional functions to this class."""
    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.length, self.n_skips, self.idf = 0, 0, 0.0
        self.skip_length = None

    def traverse_list(self):
        traversal = []
        if self.start_node is None:
            return
        else:
          node = self.start_node
          while node is not None:
            traversal.append((node.value))
            node = node.next
            """ Write logic to traverse the linked list.
                To be implemented."""
            
          return traversal

    def traverse_skips(self):
        traversal = []
        if self.start_node is None:
            return
        else:
            """ Write logic to traverse the linked list using skip pointers.
                To be implemented."""
            node = self.start_node
            while node is not None:
              traversal.append(node.value)
              node = node.skip
            return traversal

    def tfidf_values(self):
      value = []
      node = self.start_node
      if self.start_node is None:
        return []
      else:
        while node is not None:
          value.append(node.tfidf)
          node = node.next

        return value


    def add_skip_connections(self):
        n_skips = math.floor(math.sqrt(self.length))
        if n_skips * n_skips == self.length:
            n_skips = n_skips - 1
        """ Write logic to add skip pointers to the linked list. 
            This function does not return anything.
            To be implemented."""
        # raise NotImplementedError
        node = self.start_node
        top = self.start_node
        count = 0
        val = 0
        while node is not None and count<=n_skips:
          if val==0:
            top.skip = node
            top = node
          elif val == n_skips + 1:
            top.skip = node
            top = node
            val = 0
            count += 1
          val += 1
          node = node.next
        # print(n_skips)

    def calc_tf(self,tfdict):
      # print("Hello")
      if self.start_node is not None:
        node = self.start_node
        for i in tfdict.values():
          if node is not None:
            node.tfidf = i * (5000/self.length)
            node = node.next

      

    def insert_at_end(self, value):
        """ Write logic to add new elements to the linked list.
            Insert the element at an appropriate position, such that elements to the left are lower than the inserted
            element, and elements to the right are greater than the inserted element.
            To be implemented. """
        temp = Node(value)
        # print(temp.value)
        temp.next = None
        if self.start_node is None:
          self.start_node = temp
          self.end_node = temp
          # print("done")
        elif self.start_node.value >= value:
          temp.next = self.start_node
          self.start_node = temp
          # print("done")
        elif self.end_node.value <= value:
          self.end_node.next = temp
          self.end_node = temp
          # print("done")
        else:
          node = self.start_node
          prev_node = self.start_node
          while node.next is not None and node.value<value:
            prev_node = node
            node = node.next
          prev_node.next = temp
          temp.next = node
          # print("done")
        self.length += 1
        # raise NotImplementedError

