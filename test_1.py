import json
import datetime as dt

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

with open('templates.json', 'w') as f:
    f.write(json.dumps(latitude))

with open('templates.json') as f:
    print(f.read())

a = (1 << 80) - 2
print(a)
a = a.to_bytes(10, 'little')
print(a)
a = a + b'\x01'
print(a)
print(a)

