class Array(object):

    def __init__(self, capacity=10):
        self._size = 0
        self._data = [None] * capacity

    @property
    def size(self):
        return self._size

    @property
    def capacity(self):
        return len(self._data)

    def addLast(self, item):
        self.addIndex(self._size, item)

    def addIndex(self, index, item):
        if index < 0 or index >= self.capacity:
            raise ArgumentException("Index can't < 0 or >= capacity")
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = item
        self._size += 1

    def addFirst(self, item):
        self.addIndex(0, item)

    def __str__(self):
        s = 'Array: ['
        for i in range(self.size):
            s += str(self._data[i])
            if i == self.size - 1:
                break
            s += ','
        s += ']'
        return s + ', size: {}, capacity: {}'.format(self.size, self.capacity)

    def __repr__(self):
        return self.__str__

    def get(self, index):
        if index < 0 or index >= self.size:
            raise ArgumentException("Index can't < 0 or >= capacity")
        return self._data[index]

    def update(self, index, item):
        if index < 0 or index >= self.size:
            raise ArgumentException("Index can't < 0 or >= capacity")
        self._data[index] = item

    def is_contain(self, item):
        index = self.find(item)
        if index == -1:
            return False
        else:
            return index

    def find(self, item):
        for i in range(self.size):
            if self._data[i] == item:
                return i
        return -1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise ArgumentException("Index can't < 0 or >= capacity")
        item = self._data[index]
        for i in range(index, self.size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        if self.size == int(self.capacity / 4) and int(self.capacity / 2) != 0:
            self._resize(int(self.capacity / 2))
        return item

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self._size - 1)

    def removeElement(self, item):
        index = self.find(item)
        if index != -1:
            self.remove(index)

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[i]
        self._data = new_data


class ArgumentException(Exception):
    pass


if __name__ == '__main__':
    arr = Array()

    for i in range(10):
        arr.addIndex(i, i)

    print(arr)
    arr.addFirst('abc')
    print(arr)
    arr.remove(9)
    print(arr)
    arr.removeElement('abc')
    print(arr)
