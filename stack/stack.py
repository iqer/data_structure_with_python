from stack.array import Array


class ArrayStack(Array):
    def __init__(self, capacity=10):
        self.array = Array(capacity)

    def get_size(self):
        return self.array.size

    def is_empty(self):
        return self.array.isEmpty()

    def get_capacity(self):
        return self.array.capacity

    def push(self, item):
        self.array.addLast(item)

    def pop(self):
        return self.array.removeLast()

    def peek(self):
        return self.array.get_last()

    def __str__(self):
        s = 'Stack: ['
        for i in range(self.array.size):
            s += str(self.array._data[i])
            if i != self.array.size - 1:
                s += ', '
        s += '] top'
        return s

    def __repr__(self):
        return self.__str__


if __name__ == '__main__':
    arr_stack = ArrayStack()
    for i in range(5):
        arr_stack.push(i)
        print(arr_stack)

    print(arr_stack)

    arr_stack.pop()

    print(arr_stack)
