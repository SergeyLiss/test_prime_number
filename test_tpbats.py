from datetime import datetime as dt
from random import randint
from os.path import isfile
import multiprocessing as mps
from typing import Any
from tpbats import *
from numeral_system_2_10 import *

class Primer():

    def __init__(self, start_exp, prime_limit):
        self.exp = start_exp                                # Степень
        self.number_start = (1 << (1 << self.exp))          # Минимальное число
        self.number_finish = (1 << (1 << (self.exp + 1)))   # Максимальное число
        self.prime = 0                                      # Простое число
        self.prime_limit = prime_limit                      # Лимит простых чисел
        self.file_limit = 0x401                             # Лимит файлов = 1000
        self.file_position = 0x0                            # Текущий файл
        self.prime_list = [3]                               # Список простых чисел
        self.test_prime = PT()                              # Класс на проверку простоты
        self.translate = NumSys()                           # Класс для перевода в десятеричную систему счисления
        self.logs = ''                                      # Строка для вывода на экран
        self.time_now = dt.now()                            #

        self.lock: object                                   #
        pass

    def __call__(self):
        self.generate_prime()

        with mps.Pool(mps.cpu_count()) as pool:
            self.logs = f'cpu_count= {mps.cpu_count()}'
            self.print_console()
            self.lock = mps.RLock()
            pool.apply_async(self.start_search_prime())
            pool.close()
            pool.join()
        pass
    
    def generate_prime(self):
        size_pl = 1
        for i in range(5, self.prime_limit, 2):
            temp = True
            j = 0
            while temp:
                if i % self.prime_list[j] == 0:
                    temp = False
                j += 1
                if j == size_pl:
                    size_pl += 1
                    self.prime_list.append(i)
                    temp = False
        pass
    
    def prime_to_file(self):
        puth = f'D:\Desktop\Теории\Тест простоты\prime_{self.exp}\prime_{self.exp}_'
        
        flag = True
        while flag:
            file_puth = puth + str(hex(self.file_position))[2:] + '.txt'
            if not isfile(file_puth):
                flag = False
                puth = file_puth
            self.file_position += 1
        
        with open(puth, '+w') as file:
            file.write(self.translate(self.prime, True))
        pass

    def poisk_prime(self):
        flag = True
        
        for j in self.prime_list:
            if self.prime % j == 0:
                flag = False
                break
        if flag:
            self.time_now = dt.now()
            flag = self.test_prime(self.prime)
            self.logs += f'\ntime= {(dt.now() - self.time_now)}'
            # with self.lock:
            self.print_console()
        else:
            self.logs += '#'
        
        return flag
    
    def start_search_prime(self):
        self.time_now = dt.now()
        while self.file_position < self.file_limit:
            flag = False
            self.prime = randint(self.number_start, self.number_finish)
            
            if not (self.prime & 1):
                self.prime += 1
            
            while not flag:
                self.prime += 2
                
                flag = self.poisk_prime()
                
                if flag:
                    with self.lock:
                        self.prime_to_file()
        pass

    def print_console(self):
        print(self.logs)
        self.logs = ''
        pass
        
if __name__ == '__main__':
    runner = Primer(11, 1_000_000)
    runner.generate_prime()
    print('time gen prime = ', (dt.now() - runner.time_now))
    print("prime is ready", len(runner.prime_list))
    # runner.start_search_prime()
    runner()
    print('FINISH')