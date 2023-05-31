#!/usr/bin/python3
"""This module defines two classes: Node and SinglyLinkedList"""


class Node:
    """Node: defines the node of a singly linked list
        Attributes:
            __data: (int) - value stored in the node
            __next_node: (Node) - pointer to next node in the list
        Properties:
            data: Node data
            next_node: pointer to next node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data: getter/setter for __data
            Raises:
                TypeError: if data is not an integer
        """
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node: getter/setter for __next_node
            Raises:
                TypeError: if next_node is not a Node object or None
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList - defines a singly linked list
        Attributes:
            __head: head of the linked list
        Methods:
            sorted_insert: inserts a node at a sorted position
    """

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """sorted_inserts: inserts value at the correct sorted position"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.next_node is None:
            if value < self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                self.__head.next_node = new_node
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            prev = self.__head
            curr = self.__head.next_node
            while curr is not None:
                if value < curr.data:
                    new_node.next_node = curr
                    prev.next_node = new_node
                    return
                prev = curr
                curr = curr.next_node
            else:
                prev.next_node = new_node

    def __str__(self):
        """__str__: returns a string representing the singly linked list"""
        sll = ""
        runner = self.__head
        while runner is not None:
            sll += "{}".format(runner.data)
            if runner.next_node is not None:
                sll += "\n"
            runner = runner.next_node
        return sll
