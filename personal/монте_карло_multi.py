from multiprocessing import Process, Pool
import random

def foo():
    global p_circle
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2) < 1:
        p_circle += 1

def foo_bar(i):
    x = random.random()
    y = random.random()
    if (x ** 2 + y ** 2) < 1:
        return 1
    else:
        return 0


def use_pool():
    pool = Pool()
    p_circle = sum(pool.map(foo_bar, range(p_all)))
    return p_circle

def use_process():
    procs = []
    for i in range(p_all):
        proc = Process(target=foo)
        procs.append(proc)
        proc.start()
        for proc in procs:
            proc.join()

if __name__ == '__main__':
    p_all = 100_000_000
    p_circle = use_pool()
    S_circle = 4 * p_circle / p_all
    print(S_circle)
