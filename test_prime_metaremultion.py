#
import datetime
from tpbats import *
from numeral_system_2_10 import *

class MetaReMultion():

    def __init__(self):
        self.test = PT()
        self.translate = NumSys()
        self.mrm = []
        self.prime_limit = 270
        self.prime_list = [3]
        pass

    def __call__(self, msn):
        self.max_size_number = msn
        number = 0
        self.generate_prime()
        self.mrm = self.add_multiseven(number)
        return self.mrm
    
    def add_multiseven(self, number1):
        # number = number * 10 + 2
        number1 = (number1 << 2) + number1
        number1 += 1
        number1 <<= 1

        #
        max_index = self.max_size_number - len(self.translate(number1, True))
        #
        list_posev = []

        for i in range(max_index):
            # number = number * 10 + 7
            number1 = (number1 << 2) + number1
            number1 <<= 1
            number1 += 7

            if self.poisk_prime(number1):
                list_subpos = []
                list_subpos.append((i+1))
                temp = self.add_multiseven(number1)
                if temp != []:
                    list_subpos.append(temp)
                if len(list_subpos) == 1:
                        list_subpos = list_subpos[0]
                list_posev.append(list_subpos)
                

        return list_posev
    
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
        
        print("prime_count=", size_pl)
    
    def poisk_prime(self, y):
        z = True
        
        for j in self.prime_list:
            if y % j == 0:
                z = False
                break
        
        if z:
            z = self.test(y)
        
        return z


test_mrm = MetaReMultion()

list_out = test_mrm(1000)

def interpretator(otstup, list_in):
    for i in list_in:
        if type(i) != list:
            print(otstup, i)
        
        else:
            otstup += '_'
            interpretator(otstup, i)

print(list_out)
# interpretator('', list_out)