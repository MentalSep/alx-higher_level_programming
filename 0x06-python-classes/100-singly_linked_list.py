#!/usr/bin/python3
"""this module creates a Node class that defines a node
of a singly linked list and a SinglyLinkedList class"""


class Node:
    """Node class with private attributes - data, next_node"""
    def __init__(self, data, next_node=None):
        """initialize the private attributes"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """returns the data in the node"""
        return self.__data

    @data.setter
    def data(self, value):
        """this function sets the data of the node"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """"returns the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """this function set the next node of the singly linked list"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list class"""
    def __init__(self):
        """initialize the private attribute head"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None:
                if tmp.next_node.data > value:
                    break
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """returns the string representation of the singly linked list"""
        tmp = self.__head
        string = ""
        while tmp is not None:
            string += str(tmp.data) + '\n'
            tmp = tmp.next_node
        return string[:-1]
