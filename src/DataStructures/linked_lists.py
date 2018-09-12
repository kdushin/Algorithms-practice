class SinglyNode:
    def __init__(self, val, next_node=None):
        self.value = val
        self.next = next_node

    @property
    def get_value(self):
        return self.value

    @property
    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


class SinglyLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def add(self, val):
        new_node = SinglyNode(val)
        new_node.set_next(self.head)
        self.head = new_node

    def add_to_last(self, val):
        new_node = SinglyNode(val)
        current = self.head
        if current is None:
            self.head = new_node
            return

        is_end = False
        while current and is_end is False:
            next_item = current.get_next
            if next_item is None:
                is_end = True
            else:
                current = next_item

        current.set_next(new_node)

    def count(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next
        return count

    def search(self, val):
        assert isinstance(val, SinglyNode)
        current = self.head
        found = False
        while current and found is False:
            if current.get_value == val:
                found = True
            else:
                current = current.get_next
        if current is None:
            raise ValueError("Target value wasn't found in list")
        return current

    def delete(self, val):
        assert isinstance(val, SinglyNode)
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_value == val:
                found = True
            else:
                previous = current
                current = current.get_next
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next
        else:
            previous.set_next(current.get_next)


class DoublyNode:
    def __init__(self, val=None, next_node=None, prev_node=None, is_sentinel=False):
        self.prev = prev_node
        self.value = val
        self.next = next_node
        self.is_sentinel = is_sentinel

    @property
    def get_value(self):
        return self.value

    @property
    def get_next(self):
        return self.next

    @property
    def get_prev(self):
        return self.prev

    def set_next(self, next_node):
        self.next = next_node

    def set_prev(self, prev_node):
        self.prev = prev_node

    def is_sentinel(self):
        return self.is_sentinel


class DoublyLinkedList:
    def __init__(self, head=None):
        assert isinstance(head, DoublyNode)
        sent = DoublyNode(is_sentinel=True)
        if head is None:
            sent.set_next(sent)
        else:
            sent.set_next(head)
            head.set_next(sent)
        sent.set_prev(sent.get_next)
        self.sent = sent

    def add(self, val):
        new_node = DoublyNode(val)
        new_node.set_next(self.sent.get_next)
        sent_next = self.sent.get_next
        sent_next.set_prev(new_node)
        self.sent.set_next(new_node)
        new_node.set_prev(self.sent)

    def search(self, val):
        assert isinstance(val, DoublyNode)
        current = self.sent.get_next
        found = False
        while current and found is False:
            if current.is_sentinel() is False and current.get_value == val:
                found = True
            else:
                current = current.get_next
        if current is None:
            raise ValueError("Target value wasn't found in list")
        return current

    def delete(self, val):
        assert isinstance(val, DoublyNode)
        current = self.sent.get_next
        found = False
        while current and found is False:
            if current.is_sentinel() is False and current.get_value == val:
                found = True
                prev_node = current.get_prev
                next_node = current.get_next
                prev_node.set_next(next_node)
                next_node.set_prev(prev_node)
            else:
                current = current.get_next
        if current is None:
            raise ValueError("Target value wasn't found in list")
