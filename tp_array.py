# Формирование списка простых

from typing import Any


class LPN: # List Prime Number
    list_prime = [2]

    def __init__(self) -> None:
        pass

    def __call__(self, number):
        for i in range(3,number,2):
            flag = True
            for j in self.list_prime:
                if flag:
                    if (i % j) == 0:
                        flag = False
            if flag:
                self.list_prime.append(i)
        pass