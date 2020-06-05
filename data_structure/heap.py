import heapq
import math
from typing import Any


class MinHeap:
    def __init__(self):
        self.heap = []

    def list_heapify(self, input_list: list) -> None:
        heapq.heapify(input_list)
        self.heap = input_list

    @staticmethod
    def get_parent_location(i: int) -> int:
        location_i = (i - 1) // 2
        return location_i

    def insert(self, value: Any) -> None:
        heapq.heappush(self.heap, value)

    def decrease_key(self, i: int, value: Any) -> None:
        self.heap[i] = value
        parent = self.get_parent_location(i)
        while i != 0 and self.heap[parent] > self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

    def extract_min(self) -> Any:
        return heapq.heappop(self.heap)

    def delete_key(self, i) -> None:
        self.decrease_key(i, math.inf)
        self.extract_min()

    def get_min(self) -> Any:
        return self.heap[0]


def heap_sort(input_list: list) -> list:
    heap = MinHeap()
    heap.list_heapify(input_list)
    sorted_list = [heap.extract_min() for _ in range(len(input_list))]
    return sorted_list


if __name__ == '__main__':
    print(heap_sort([1, 3, 5, 7, 0, 2]))
