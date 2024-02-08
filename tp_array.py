# Формирование списка простых
import multiprocessing as mps
from datetime import datetime as dt

class LPN: # List Prime Number
    list_prime = [2, 3, 5, 7]

    def __init__(self) -> None:
        self.cpu_count = mps.cpu_count() - 1
        # self.bar = mps.Barrier(self.cpu_count)
        pass

    def __call__(self, number):
        with mps.Pool(self.cpu_count) as p:
            for i in range(9,number,2):
                p.apply_async(self.prime_search, args=(i,), callback=self.list_add)
            p.close()
            p.join() 
        pass

    def list_add(self, prime):
        if prime != 0:
            self.list_prime.append(prime)
        pass

    def prime_search(self, prjme):
        for i in self.list_prime:
            if (prjme % i) == 0:
                return 0
        return prjme


if __name__ == "__main__":
    size = 1000
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