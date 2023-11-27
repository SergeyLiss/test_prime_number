# Перевод из одной системы счисления в другую (2 и 10)

class NumSys():
    numsys_int: int # Число
    numsys_bin_str: str # Представление числа в двоичной системе счисления
    symbol: int # Заданная система счисления (по умолчанию 10)
    numsys_symbol_str: str # Представление числа в заданной системе счисления
    sys_dict: dict # Словарь сумм в заданной системе счисления
    abc = '0123456789abcdefghijklmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ._+=' # Алфавит системы счисления (max = 64 symbol)

    def __init__(self):
        self.symbol = 10
        pass

    def __call__(self, input_num, flag=False):
        if flag: # 2 -> 10
            # self.numsys_bin_str = input_num
            # self.translation_bin_str_to_bin()
            self.numsys_int = input_num
            # self.number_to_binary_string()
            self.translation_bin_to_symbol()
            return self.numsys_symbol_str
        else: # 10 -> 2
            self.numsys_symbol_str = input_num
            self.translation_10to2()
            return self.numsys_int

    def translation_10to2(self): # Перевод представления числа в 10-тичной системы счисления в число
        self.numsys_int = 0
        for item in self.numsys_symbol_str:
            self.numsys_int = (self.numsys_int << 2) + self.numsys_int
            self.numsys_int <<= 1
            self.numsys_int += int(item)
        pass

    def translation_bin_str_to_bin(self):
        self.numsys_int = 0
        for item in self.numsys_bin_str:
            self.numsys_int = self.numsys_int << 1
            self.numsys_int += int(item)
        pass

    def translation_bin_to_symbol(self):
        self.numsys_symbol_str = ''
        temp_number = self.numsys_int
        while temp_number != 0:
            temp_x = temp_number % self.symbol
            temp_number //= self.symbol
            self.numsys_symbol_str = self.abc[temp_x] + self.numsys_symbol_str
        pass
    # def translation_bin_to_symbol(self):
    #     self.sys_dict = self.generation_dict_abc(self.symbol)
    #     numsys_symbol_list_str = ['0']
    #     size_numsys_symbol_str = 1
    #     for item in self.numsys_bin_str:
    #         list_flag = [False]

    #         for i in range(size_numsys_symbol_str):
    #             temp_i = self.sys_dict[numsys_symbol_list_str[i]][numsys_symbol_list_str[i]]
    #             numsys_symbol_list_str[i] = temp_i[0]
    #             list_flag.append(temp_i[1])
            
    #         if list_flag[-1]:
    #             numsys_symbol_list_str.append('0')
    #             size_numsys_symbol_str += 1
            
    #         for j in range(size_numsys_symbol_str):
    #             if list_flag[j]:
    #                 temp_j = self.sys_dict[numsys_symbol_list_str[j]]['1']
    #                 numsys_symbol_list_str[j] = temp_j[0]
    #                 k = 1
    #                 while temp_j[1]:
    #                     temp_j = self.sys_dict[numsys_symbol_list_str[j+k]]['1']
    #                     numsys_symbol_list_str[j+k] = temp_j[0]
    #                     k += 1
    #         numsys_symbol_list_str[0] = self.sys_dict[numsys_symbol_list_str[0]][item][0]
        
    #     self.numsys_symbol_str = ''.join(reversed(numsys_symbol_list_str))
    #     pass

    def generation_dict_abc(self, num_sys): # Создание словаря сумм для заданной системы счисления
        return {
            self.abc[i]: {
                self.abc[j]:
                    [self.abc[(i+j)%num_sys], (True if (i+j) >= num_sys else False)]
                for j in range(num_sys) }
            for i in range(num_sys) }
    
    def number_to_binary_string(self): # Перевод числа в двоичное представление
        self.numsys_bin_str = bin(self.numsys_int)[2:]
        pass
    # def number_to_binary_string(self):
    #     temp_number = self.numsys_int
    #     while temp_number != 0:
    #         self.numsys_bin_str = self.abc[(temp_number & 1)] + self.numsys_bin_str
    #         temp_number >>= 1
    #     pass