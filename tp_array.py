# Формирование списка простых
import multiprocessing as mps
from datetime import datetime as dt
import time

class LPN: # List Prime Number

    def __init__(self) -> None:
        self.cpu_count = mps.cpu_count()
        self.list_prime = mps.Manager().list()
        self.iter = mps.Manager().Value('i', 3)
        self.lock = mps.Manager().RLock()
        self.semafor = mps.Manager().BoundedSemaphore(1)
        self.number = 0
        self.processes = []
        pass

    def __call__(self, number):
        self.number = number
        self.list_prime.append(3)
        with mps.Pool(self.cpu_count) as pool:
            while self.iter.value < self.number:
                pool.apply_async(self.list_add, args=(self.prime_search(),))
                self.iter.value += 2
                
            
            pool.close()
            pool.join()
        
        pass

    def list_add(self, prime):
        if prime != 0:
            self.semafor.acquire()
            temp = self.list_prime
            temp.append(prime)
            self.list_prime = temp
            # self.list_prime.append(prime)
            self.semafor.release()
        pass

    def prime_search(self):
        for i in self.list_prime:
            if (self.iter.value % i) == 0:
                return 0
        return self.iter.value


if __name__ == "__main__":
    size = 100
    start = dt.now()
    test = LPN()
    test(size)
    print(f"number_count= {size}")
    print(f"prime_count= {len(test.list_prime)}")
    print(f"time= {dt.now()-start}")
    print(f"cpu_count= {test.cpu_count}")
    print(test.list_prime)





# class LPN: # List Prime Number
#     list_prime = [2]

#     def __init__(self) -> None:
#         pass

#     def __call__(self, number):
#         for i in range(3,number,2):
#             flag = True
#             for j in self.list_prime:
#                 if flag:
#                     if (i % j) == 0:
#                         flag = False
#             if flag:
#                 self.list_prime.append(i)
#         pass