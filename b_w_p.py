# how to share data between 2 processor
# By shared memory the memory lives outside the process and for access it and fetch data from there
# using 2 types of methods then we can achieve it, 1 is value another is array.
import time
import multiprocessing


def cal_sq(n, square,v):
    v.value=10.5
    for i, j in enumerate(n):
        square[i] = j * j


if __name__ == "__main__":
    arr = [2, 3, 4]
    square = multiprocessing.Array('i', 3)# type length
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=cal_sq, args=(arr, square,v))

    p1.start()

    p1.join()
    print("result", square[:])
    print("result",v.value)
    print("Done")
