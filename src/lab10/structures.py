from collections import deque
from typing import Any

class Queue:
    def __init__(self):
        self._data: deque[Any] = deque()

    def enqueue(self, item) -> None:
        self._data.appendleft(item)

    def dequeue(self) -> Any:
        if self.__len__ == 0:
            raise IndexError("")
        return self._data.pop()

    def peak(self) -> Any | None:
        if self.__len__ == 0:
            raise IndexError("")
        return self._data[-1]

    def is_empty(self) -> bool:
        if self.__len__ == 0:
            return True
        return False

    def __len__(self) -> int:
        return len(self._data)


class Stack:
    def __init__(self):
        self._data: list[Any] = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self) -> Any:
        if self.__len__ == 0:
            raise IndexError("Sosi pissy")
        return self._data.pop()

    def peek(self) -> Any | None:
        if self.__len__ == 0:
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        if self.__len__ == 0:
            return True
        return False

    def __len__(self) -> int:
        return len(self._data)