from my_array import Array


class Queue(Array):

    def __init__(self, capacity=10):
        super(Queue, self).__init__(capacity)

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    def is_empty(self):
        return self.isEmpty()

    def dequeue(self):
        return self.removeFirst()

    def enqueue(self, item):
        return self.addLast(item)

    def __str__(self):
        res = 'Queue: size = %s, capacity = %s\n' % (self.size, self.capacity)
        res += 'front ['
        for i in range(self.size):
            res += str(self._data[i])
            if i != self.size - 1:
                res += ', '
        res += '] tail'
        return res

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":
    queue = Queue()
    for i in range(10):
        queue.enqueue(i)
        print(queue)

        if (i % 3) == 2:
            queue.dequeue()
            print(queue)
