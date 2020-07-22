import multiprocessing


def cal_sq(n, q):
    for i in n:
        q.put(i * i)


if __name__ == "__main__":
    arr = [2, 3, 4]
    q = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=cal_sq, args=(arr, q,))

    p1.start()
    p1.join()
    while q.empty() is False:
        print(q.get())

## ###  multiprocessing
# q = multiprocessing.Queue()
# -->lives in shared memory
# -->used to share data between process

##### queue module
# import queue
# q = queue.Queue()
# lives in in-process memory
# used to share data between threads
