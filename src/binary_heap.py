class Heap:
    def __init__(self, array):
        assert isinstance(array, list)
        self.Array = array
        self.HeapSize = len(array)

    def __getitem__(self, key):
        return self.Array[key - 1]

    def __setitem__(self, key, value):
        self.Array[key - 1] = value

    def sort(self):
        if len(self.Array) < 2:
            return

        self.build_heap()

        while self.HeapSize > 1:
            self.swap_items(1, self.HeapSize)
            self.HeapSize -= 1
            self.heapify(1)

    @staticmethod
    def get_parent_index(index):
        return index >> 1

    @staticmethod
    def get_left_child_index(index):
        return index << 1

    @staticmethod
    def get_right_child_index(index):
        return (index << 1) + 1

    def swap_items(self, first_index, second_index):
        temp = self[first_index]
        self[first_index] = self[second_index]
        self[second_index] = temp

    def heapify(self, parent_index):
        while True:
            left = self.get_left_child_index(parent_index)
            right = self.get_right_child_index(parent_index)
            largest = parent_index

            if left <= self.HeapSize and self[left] > self[largest]:
                largest = left

            if right <= self.HeapSize and self[right] > self[largest]:
                largest = right

            if largest != parent_index:
                self.swap_items(parent_index, largest)
                parent_index = largest
            else:
                return

    def build_heap(self):
        start_index = self.HeapSize // 2

        for i in range(start_index, 0, -1):
            self.heapify(i)

    def extract_max(self):
        if self.HeapSize < 1:
            raise RuntimeError
        max_val = self[1]
        self[1] = self[self.HeapSize]
        self.HeapSize = self.HeapSize - 1
        self.heapify(1)
        return max_val

    def max_insert(self, key):
        self.HeapSize = self.HeapSize + 1
        i = self.HeapSize
        if self.HeapSize > len(self.Array):
            self.Array.append(self[self.get_parent_index(i)])
        self.increase_key(i, key)

    def increase_key(self, i, k):
        if k < self[i]:
            raise RuntimeError
        else:
            while i > 1 and self[self.get_parent_index(i)] < k:
                self[i] = self[self.get_parent_index(i)]
                i = self.get_parent_index(i)
            self[i] = k
