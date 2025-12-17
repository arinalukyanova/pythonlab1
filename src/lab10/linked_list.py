class Node:
    def __init__(self, value: any, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self, head: Node, tail: Node):
        self.head = None
        self.tail = None
        self._size: int = 0

    def append(self, value: any) -> None:
        new = Node(value, None)
        if self.head == None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
        self._size += 1

    def prepend(self, value: any) -> None:
        new = Node(value, self.head)
        self.head = new
        if self.tail == None:
            self.tail = new
        self._size += 1

    def insert(self, idx: int, value: any) -> None:
        if not (0 < idx < self.__len__):
            raise IndexError("")
        cur = self.head
        for i in range(idx - 1):
            cur = cur.next
        new = Node(value, None)
        new.next = cur.next
        cur.next = new
        self._size += 1

    def remove(self, value: any) -> None:
        if self.head == None:
            return
        old = cur
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                if cur.next is None:
                    self.tail = cur
                self._size -= 1
                return
            cur = cur.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self) -> int:
        return self._size

    def __rerp__(self) -> str:
        return f"SinglyLinkedList({list(self)})"