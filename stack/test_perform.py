import time
import random
import sys

from demo_queue import Queue
from loop_queue import LoopQueue


# 出队的复杂度,特别需要注意
def test_queue(q, loop_count):
    t1 = time.time()
    for i in range(loop_count):
        q.enqueue(random.randint(0, sys.maxsize))
    for i in range(loop_count):
        q.dequeue()

    t2 = time.time()

    return t2 - t1


if __name__ == "__main__":
    loop_count = 100000
    array_queue = Queue()
    t1 = test_queue(array_queue, loop_count)
    print('ArrayQueue, time', t1, 's')
    loop_queue = LoopQueue()
    t2 = test_queue(loop_queue, loop_count)
    print('Loop_queue, time', t2, 's')
