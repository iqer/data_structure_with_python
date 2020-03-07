class Array:

    def __init__(self, capacity):
        self._size = 0
        self._data = [None] * capacity

    # 返回数组当前大小
    @property
    def size(self):
        return self._size

    # 返回数组容量
    @property
    def capacity(self):
        return len(self._data)

    def isEmpty(self):
        return self.size == 0

    # 向数组末尾添加元素
    def addLast(self, item):
        self.addIndex(self.size, item)

    def addFirst(self, item):
        self.addIndex(0, item)

    def addIndex(self, index, item):
        if index < 0 or index > self.size:
            raise ArgumentException(
                'Add failed. Require index >= 0 and index <= size')
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        if index < self.capacity - 1 and self.size < self.capacity - 1 and \
                index <= self.size:
            for i in range(self.size - 1, index - 1, -1):
                self._data[i + 1] = self._data[i]
            self._data[index] = item
            self._size += 1

    def resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[i]
        self._data = new_data

    def get(self, index):
        if index < 0 and index >= self.size:
            raise ArgumentException(
                'Get failed. Require index >= 0 and index <= size.')
        return self._data[index]

    def set(self, index, item):
        if index < 0 and index >= self.size:
            raise ArgumentException(
                'Set failed. Require index >= 0 and index <= size.')
        self._data[index] = item

    def is_contain(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return True
        return False

    def find(self, item):
        for i in range(self._size):
            if self._data[i] == item:
                return i
        return -1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise ArgumentException(
                'Delete failed. Require index >= 0 and index <= size.')
        item = self._data[index]
        for i in range(index, self.size):
            self._data[i] = self._data[i+1]
        self._size -= 1
        # lazy缩容,让算法的整体性能更好一些
        if self.size == int(self.capacity / 4) and int(self.capacity / 2) != 0:
            self.resize(int(self.capacity / 2))
        return item

    def removeFirst(self):
        return self.remove(0)

    def removeLast(self):
        return self.remove(self._size - 1)

    def removeElement(self, item):
        index = self.find(item)
        if index != -1:
            self.remove(index)

    def __str__(self):
        res = 'Array: size = %s, capacity = %s\n' % (self.size, self.capacity)
        res += '['
        for i in range(self.size):
            res += str(self._data[i])
            if i != self.size - 1:
                res += ', '
        res += ']'
        return res


class ArgumentException(Exception):
    pass


if __name__ == "__main__":
    arr = Array(20)

    for i in range(10):
        arr.addLast(i)

    print(arr)
    arr.addIndex(1, 100)
    print(arr)
    arr.addFirst(-1)
    print(arr)
    arr.addFirst('abc')
    arr.remove(2)
    print(arr)
    arr.removeElement(4)
    arr.removeFirst()
    print(arr)
