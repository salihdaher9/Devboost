import random
import time

mylist = random.sample(range(1, 1000001), 10000)
myset=set(mylist)

def listlookups(list):

    print("start...")
    t0 = time.perf_counter()
    for i in range(10000):
        random_number = random.randint(1, 100000)
        if random_number in mylist:
            pass

    return time.perf_counter() - t0
def setlookup(set):
    print("start...")
    t0 = time.perf_counter()
    for i in range(10000):
        random_number = random.randint(1, 100000)
        if random_number in set:
            pass

    return time.perf_counter() - t0


print(listlookups(mylist))
print(setlookup(myset))