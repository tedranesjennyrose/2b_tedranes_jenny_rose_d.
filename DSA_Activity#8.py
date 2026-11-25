
# ACTIVITY 8: HEAPS AND PRIORITY QUEUES

# ==========================================
# ACTIVITY 1: MIN-HEAP
# ==========================================

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract(self):
        if not self.heap:
            return None

        minimum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                    smallest = left

                if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                    smallest = right

                if smallest == i:
                    break

                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
                i = smallest

        return minimum

    def size(self):
        return len(self.heap)


# Test Activity 1
print("ACTIVITY 1: MIN-HEAP")

numbers = [5, 9, 11, 14, 19, 17, 18, 13]
min_heap = MinHeap()

for number in numbers:
    min_heap.insert(number)

print("Peek:", min_heap.peek())
print("Size:", min_heap.size())

result = []
while min_heap.size() > 0:
    result.append(min_heap.extract())

print("Extract order:", result)


# ==========================================
# ACTIVITY 2: MAX-HEAP
# ==========================================

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def peek(self):
        return self.heap[0] if self.heap else None

    def extract(self):
        if not self.heap:
            return None

        maximum = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                    largest = left

                if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                    largest = right

                if largest == i:
                    break

                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest

        return maximum

    def size(self):
        return len(self.heap)


# Test Activity 2
print("\nACTIVITY 2: MAX-HEAP")

max_heap = MaxHeap()

for number in numbers:
    max_heap.insert(number)

result = []
while max_heap.size() > 0:
    result.append(max_heap.extract())

print("Extract order:", result)


# ==========================================
# ACTIVITY 3: HEAP SORT
# ==========================================

def heap_sort(arr):
    heap = MaxHeap()

    for number in arr:
        heap.insert(number)

    result = []

    while heap.size() > 0:
        result.append(heap.extract())

    return result


print("\nACTIVITY 3: HEAP SORT")

test_arrays = [
    [4, 10, 3, 5, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [4, 2, 4, 1, 2],
    []
]

for arr in test_arrays:
    print("Original:", arr)
    print("Sorted:", heap_sort(arr))


# ==========================================
# ACTIVITY 4: KTH LARGEST
# ==========================================

def kth_largest(numbers, k):
    if k < 1 or k > len(numbers):
        return None

    heap = MinHeap()

    for number in numbers:
        heap.insert(number)

        if heap.size() > k:
            heap.extract()

    return heap.peek()


print("\nACTIVITY 4: KTH LARGEST")

values = [7, 10, 4, 3, 20, 15]
k = 3

answer = kth_largest(values, k)

print("Numbers:", values)
print("K:", k)
print("Kth largest:", answer)
print("Verification:", sorted(values, reverse=True)[k - 1])


# ==========================================
# ACTIVITY 5: MERGE K SORTED ARRAYS
# ==========================================

def merge_k_arrays(arrays):
    heap = MinHeap()
    result = []

    for i in range(len(arrays)):
        if arrays[i]:
            heap.insert((arrays[i][0], i, 0))

    while heap.size() > 0:
        value, array_index, element_index = heap.extract()
        result.append(value)

        next_index = element_index + 1

        if next_index < len(arrays[array_index]):
            next_value = arrays[array_index][next_index]

            heap.insert((next_value, array_index, next_index))

    return result


print("\nACTIVITY 5: MERGE K SORTED ARRAYS")

arrays = [
    [1, 4, 7, 10],
    [2, 5, 8],
    [3, 6, 9, 12, 15]
]

print("Original arrays:", arrays)
print("Merged array:", merge_k_arrays(arrays))


# ==========================================
# ACTIVITY 6: PRIORITY SCHEDULER
# ==========================================

def priority_scheduler(jobs):
    heap = MaxHeap()

    for priority, job in jobs:
        heap.insert((priority, job))

    release_order = []

    while heap.size() > 0:
        priority, job = heap.extract()
        release_order.append(job)

        print("Released:", job, "| Priority:", priority)

    return release_order


print("\nACTIVITY 6: PRIORITY SCHEDULER")

jobs = [
    (2, "Job A"),
    (5, "Job B"),
    (1, "Job C"),
    (4, "Job D"),
    (3, "Job E")
]

order = priority_scheduler(jobs)

print("Final release order:", order)


# ==========================================
# ADDITIONAL TEST CASES
# EMPTY, SINGLE, DUPLICATES, RANDOM
# ==========================================

print("\nADDITIONAL HEAP TESTS")

test_cases = [
    [],
    [10],
    [5, 5, 3, 3, 8, 8],
    [12, 4, 19, 2, 15, 7, 1]
]

for case in test_cases:
    min_h = MinHeap()
    max_h = MaxHeap()

    for number in case:
        min_h.insert(number)
        max_h.insert(number)

    ascending = []
    descending = []

    while min_h.size() > 0:
        ascending.append(min_h.extract())

    while max_h.size() > 0:
        descending.append(max_h.extract())

    print("\nInput:", case)
    print("Min-heap:", ascending)
    print("Max-heap:", descending)
    print("Heap sort:", heap_sort(case))