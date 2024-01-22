# Формирование списка простых чисел в формате 30 * (file_size) + thirty[]
# Биты в байте соотносятся со списком остатков - 2^k <=> thirty[k]
# Бинарный файл размером - 4_194_304 байт
# В файле содержатся 125_829_120 чисел
# Логи - logs.json
# Файлы - number_list_k.prime, где k - итерация

from os.path import isfile

class PrimeListForm():
    #
    bytelist: list

    def __init__(self, iterable_index_file) -> None:
        #
        self.const_thirty = 30
        self.const_index = 8
        # Список остатков по модулю 30. Представленны числа, которые не делятся на множители числа 30.
        self.thirty = [1, 7, 11, 13, 17, 19, 23, 29]
        # Словарь индексов от остатков
        self.thirty_dict = {1: 0, 7: 1, 11: 2, 13: 3, 17: 4, 19: 5, 23: 6, 29: 7}
        # Трехмерный список произведений
        self.thirty_multy = [[self.del_mod(i, j) for j in range(self.const_index)] for i in range(self.const_index)]
        # Размер файла 4 Мб = 2^22
        self.file_size = 4_194_304
        # Итерационный индекс файла
        self.iif = iterable_index_file
        pass

    # 
    def file_load(self, attr):
        # Атрибуты:
        # 'r' - read
        # 'w' - write
        #

        puth_file = f'number_list_{self.iif}.prime'
        puth_log = 'logs.json'

        if attr == 'r':
            if isfile(puth_file):
                with open(puth_file, 'rb') as file:
                    self.bytelist = file.read()
            else:
                self.bytelist = bytearray(self.file_size)


        elif attr == 'w':
            if isfile(puth_file):
                with open(puth_file, 'wb') as file:
                    file.write(self.bytelist)
            else:
                with open(puth_file, 'xb') as file:
                    file.write(self.bytelist)
        
        else:
            print("error")
        pass

    #
        pass

    # Формирование списка произведений: [0] - остаток, [1] - целый делитель
    def del_mod(self, x, y):
        x = self.thirty[x]
        y = self.thirty[y]
        x = x * y
        y = x // self.const_thirty
        x = x % self.const_thirty

        return [x, y]
            
    # Восстановление 'байтового' числа
    def number_recovery_byte(self, index):
        # Число от индекса файла (self.iif) и индекса (index)
        # index = self.iif * self.file_size + index = self.iif * 2^22 + index = (self.iif << 22) + index
        # index = 30 * index
        # 30 * index = (32-2) * index = (16-1) * 2 * index
        # ((index << 4) - index) << 1
        #
        index = (self.iif << 22) + index
        index = (index << 4) - index
        index = index << 1
        
        return index

    # Вычисление корня индекса (байта)
    def sqrt_index(self, index):
        # 30a+b < 30(a+1) ~ 30a
        # index = sqrt(30a)/30 = sqrt(a/30)
        # index = index + 1
        #

        index = index / self.const_thirty
        index = pow(index, 1/2)
        index = int(index) + 1
        return index
    