import time
from functools import lru_cache


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def calcolo_elemento(self, n):
        #terminale
        if n == 0:
            return 0
        elif n == 1:
            return 1
        #caso ricorsivo
        else:
            return self.calcolo_elemento(n-1) + self.calcolo_elemento(n-2)

    @lru_cache(maxsize=None)
    def calcolo_elemento_lru(self, n):
        # terminale
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # caso ricorsivo
        else:
            return self.calcolo_elemento_lru(n - 1) + self.calcolo_elemento_lru(n - 2)

    def calcolo_elemento_cache(self, n):
        # se ho già la soluzione per questo n la prendo dalla cache
        if self.cache.get(n) is not None:
            return self.cache[n]
        #altrimenti devo andare avanti con la ricorsione
        else:
            #aggiungo nel dizionario
            self.cache[n] = self.calcolo_elemento_cache(n-1) + self.calcolo_elemento_cache(n-2)
            #restituisco il valore
            return self.cache[n]


if __name__ == '__main__':
    fib = Fibonacci()
    N = 7
    start_time = time.time()
    print(fib.calcolo_elemento(N))
    end_time = time.time()
    print(f"elapsed time - recursione normale: {end_time - start_time}")

    start_time = time.time()
    print(fib.calcolo_elemento_cache(N))
    end_time = time.time()
    print(f"elapsed time - cahce: {end_time - start_time}")

    start_time = time.time()
    print(fib.calcolo_elemento_lru(N))
    end_time = time.time()
    print(f"elapsed time - lru: {end_time - start_time}")