import math
import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def list_heapify(self, lst: list):
        heapq.heapify(lst)
        self.heap = lst

    @staticmethod
    def get_parent_location(i: int) -> int:
        location_i = (i - 1) // 2
        return location_i

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def decrease_key(self, i, value):
        self.heap[i] = value
        parent = self.get_parent_location(i)
        while i != 0 and self.heap[parent] > self.heap[i]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]

    def extract_min(self):
        return heapq.heappop(self.heap)

    def delete_key(self, i):
        self.decrease_key(i, math.inf)
        self.extract_min()

    def get_min(self):
        return self.heap[0]


def heap_sort(input_list: list) -> list:
    heap = MinHeap()
    heap.list_heapify(input_list)
    sorted_list = [heap.extract_min() for _ in range(len(input_list))]
    return sorted_list


if __name__ == '__main__':
    input_list = [1, 3, 5, 7, 0, 2]
    print(heap_sort(input_list))
