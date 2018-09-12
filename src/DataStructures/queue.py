from src.DataStructures.linked_lists import SinglyLinkedList, SinglyNode


class Queue(object):
    def __init__(self):
        self.elements = SinglyLinkedList()

    def get_last(self):
        current = self.elements.head
        assert isinstance(current, SinglyNode)
        is_end = False
        while current and is_end is False:
            next_item = current.get_next
            if next_item is None:
                is_end = True
            else:
                current = next_item
        if current is None:
            raise ValueError("Queue is empty!")
        return current


    def enqueue(self, val):
        self.elements.add()

    def dequeue(self):
        target_element = self.elements.head
        if target_element is not None:
            self.elements.delete(target_element)
        return target_element