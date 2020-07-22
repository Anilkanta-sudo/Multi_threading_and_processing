import time
import threading


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


arr = 40
t = time.time()
"""
# test with  normal functions and check time taking
print_even(arr)
print_odd(arr)
print(time.time() - t)
"""

t1 = threading.Thread(target=print_even, args=(arr,))
t2 = threading.Thread(target=print_odd, args=(arr,))

# execute the above both parelally
t1.start()  # start the threads
t2.start()  # start the threads

# will untill the done
t1.join()
t2.join()

# real time ex:
# webservice make it more responsive and optimized
# global interpreter lock
# cpu type
print(time.time() - t)
