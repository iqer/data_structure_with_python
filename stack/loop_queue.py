from demo_queue import Queue


class LoopQueue(Queue):

    def __init__(self, capacity=10):
        self._data = [None] * (capacity + 1)
        self._front = self._tail = 0
        self._size = 0

    @property
    def capacity(self):
        return len(self._data) - 1

    @property
    def size(self):
        return self._size

    def is_empty(self):
        return self._front == self._tail

    def enqueue(self, item):
        if self._front == (self._tail + 1) % self.capacity:
            self._resize(self.capacity * 2)
        self._data[self._tail] = item
        self._tail = (self._tail + 1) % self.capacity
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Cannot dequeue from an empty queue.')
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        if self._size < (self.capacity / 4) and int(self.capacity / 2) != 0:
            self._resize(int(self.capacity / 2))
        return item

    # 扩容
    def _resize(self, new_capacity):
        new_data = [None] * (new_capacity + 1)
        # for i in range(self._front, self._tail + 1):
        #     new_data[i % self.capacity] = self._data[i % self.capacity]
        for i in range(self.size):
            new_data[i] = self._data[(self._front + i) % self.capacity]
        self._data = new_data
        self._front = 0
        self._tail = self.size

    def get_front(self):
        if self.is_empty():
            raise Exception('Cannot dequeue from an empty queue.')
        return self._data[self._front]

    def __str__(self):
        res = 'Loop_queue: size = %s, capacity = %s\n' % (
            self.size, self.capacity)
        res += 'front ['
        for i in range(self._front, self._front + self._size):
            res += str(self._data[i % self.capacity])
            if i != self._front + self.size - 1:
                res += ', '
        res += '] tail'
        return res


if __name__ == "__main__":
    queue = LoopQueue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)

        if (i % 3) == 2:
            queue.dequeue()
            print(queue)
