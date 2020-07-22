import time
import multiprocessing


# store result global variable
def print_even(n):
    print("even number")
    for i in range(0, n + 1, 2):
        time.sleep(0.2)
        print("even:", i)


def print_odd(n):
    print("odd number")
    for i in range(1, n + 1, 2):
        time.sleep(0.2)
        print("odd:", i)


if __name__ == "__main__":
    t = time.time()
    arr = 40
    p1 = multiprocessing.Process(target=print_even, args=(arr,))
    p2 = multiprocessing.Process(target=print_odd, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Done")
    print(time.time() - t)

# create new copy of even
even = []


def print_even(n):
    for i in range(0, n + 1, 2):
        time.sleep(0.2)
        even.append(i)
        print("even:", i)
    print(even)


if __name__ == "__main__":
    arr = 20
    p1 = multiprocessing.Process(target=print_even, args=(arr,))

    p1.start()

    p1.join()
    print("result", even)
    print("Done")

# if you ant share data b/w 2 processors you need to use IPC techniques, then only u can share, VM allocates separate
# address spaces for each processor