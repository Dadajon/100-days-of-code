#!/bin/python3


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node):
    while node:
        print(str(node.data))
        node = node.next


def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if head:
        current = head
        while current.next:
            current = current.next
        current.next = node
    else:
        head = node
    return head


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head)
    print('\n')
