# Формирование списка простых чисел в формате 30 * (file_size) + thirty[]
# Биты в байте соотносятся со списком остатков - 2^k <=> thirty[k]
# Бинарный файл размером - 4_194_304 байт
# В файле содержатся 125_829_120 чисел
# Логи - logs.json
# Файлы - number_list_k.prime, где k - итерация

from os.path import isfile
import json

class PrimeListForm():

    def __init__(self) -> None:
        # Имя лог-файла, лог-файл
        self.name_log = 'templates.json'
        self.log_file = []
        # Флаг остановки алгоритма
        self.flag_exit = True
        # Константы
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
        self.iif = 0
        #
        self.file_name = ''
        #
        self.bytelist = b''
        pass

    #
    def __call__(self):
        self.open_file(self.name_log, 'r')

        self.file_name = self.log_file['all']['directory'] \
                        + self.log_file['all']['file_prefix'] \
                        + str(self.log_file['now']['file_id']) \
                        + self.log_file['all']['file_suffix']
        
        self.open_file(self.file_name, 'br')

        self.algoritm()


        pass

    #
    def algoritm(self):
        pass
    #
    def open_file(self, name, attr):
        if isfile(name):
            with open(name, attr) as file:
                match attr:
                    case 'r':
                        self.log_file = file.read()
                    case 'w':
                        file.write(json.dumps(self.log_file))
                    case 'br':
                        self.bytelist = file.read()
                    case 'bw':
                        file.write(self.bytelist)
        else:
            with open(name, attr) as file:
                if name == self.name_log:
                    self.log_file = self.create_log()
                    file.write(json.dumps(self.log_file))
                else:
                    self.exceptions(0, name)
                    self.byte_list_null()
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
    
    #
    def byte_list_null(self):
        temp = self.file_size << 3
        temp = temp + 1
        temp = 1 << temp
        temp = temp - 1
        if self.log_file['now']['file_id'] == 0:
            temp = temp - 1
        self.bytelist = temp.to_bytes(self.file_size, 'little')

    #
    def exceptions(self, cod, name=None):
        match cod:
            case 0:
                print(f"Файл {name} создан...")
    
    #
    def create_log(self):
        latitude = {
            'now':                                  # В процессе сортировки
            {
                'file_id': 0,                       # Текущий файл в обработке
                'file_position': 1,                 # Текущая позиция в обработке
                'sqrt_position': 0,                 # Текущая позиция от корня
            },
            
            'all':                                  # Характеристика по всем файлам
            {
                'directory': 'data/',               # Директория хранения файлов
                'file_prefix': 'number_list_',      # Часть имени файла -> Префикс
                'file_suffix': '.prime',            # Расширение файла -> Суффикс
                'prime': 10,                        # Количество простых чисел во всех файлах. Начальное значение - 10, количество простых чисел до 30.
                'prime_list': [2, 3, 5],            # Начальные простые числа. Не включены в базу файлов. Делители числа 30.
                'file_id': 0                        # Количество обработаных файлов
            }
        }
        return json.dumps(latitude)

    