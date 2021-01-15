import string
import random
import math

class Rsa:
    def __init__(self):
        # define character and values
        self.all_character = self.define_all_character()
        # define primary number
        self.all_primary_number = [2, 3, 5, 7]
        self.selected_prime = 0
        
        # make the rsa modulus (p*q)
        self.p = self.choose_prime_number()
        self.q = self.choose_prime_number()

        # define rsa modulus
        self.rsa_modulus = self.p*self.q
        print(self.p, self.q, self.rsa_modulus)

        # define fi function -> p-1 * q-1
        self.fi = (self.p-1)*(self.q-1)
        
        # define derived number (e)
        # derived number must be greater than 1 and less than the (p-1)(q-1). it also has to be co-prime with modulus, and fi function
        self.derived_number = self.define_derived_number(self.rsa_modulus,self.fi)
        print(self.derived_number)

        # define the lock (e, modulus)
        self.the_lock = [self.derived_number, self.rsa_modulus]

        # define private key 
        self.private_key = self.get_private_key(self.the_lock, self.fi)

        self.private_lock = [self.private_key, self.rsa_modulus]
    # 1. generate rsa modulus
    def define_all_character(self):
        return dict(zip(string.ascii_lowercase, range(0,26)))
    
    # 2. choose random prime number
    def choose_prime_number(self):
        num = random.choice(self.all_primary_number)
        if num != self.selected_prime:
            self.selected_prime = num
            return num
        else:
            return self.choose_prime_number()
    
    def define_derived_number(self, md, fi):
        list_coprime = list()
        for i in range(2,fi):
            if self.is_coprime(i,md) and self.is_coprime(i, fi):
                list_coprime.append(i)
        if list_coprime is None:
            return self.__init__()
        return random.choice(list_coprime)
    def gcd(self,p,q):
        while q != 0:
            p, q = q, p%q
        return p

    def is_coprime(self,x,y):
        return self.gcd(x,y) == 1

    def encrypt_text(self, text):
        self.text = text
        repre_number = list()
        chiper_text = ''
        
        for t in text:
            # change character to the representative number
            for k, v in self.all_character.items():
                if k == t:
                    repre_number.append(v)
        
        print(self.the_lock)
        for r in repre_number:
            repre_val = int(math.pow(r, self.the_lock[0])%self.the_lock[1])
            for k, v in self.all_character.items():
                if v == repre_val:
                    chiper_text+=k
        self.chiper_text = chiper_text
        print('-'*10)
        print('enkri text : ', self.chiper_text)
        print('-'*10)
    
    def get_private_key(self, lock, fi):
        print('e : ', lock[0])
        print('fi : ', fi)
        d = 1
        while (lock[0]*d)%fi != 1:
            d = d+(fi-1)
        return d
    
    def decrypt_text(self):
        print('lock public : ', self.the_lock)
        print('lock : ', self.private_lock)
        decrypted_list = list()
        decrypted_text = ''
        # take the chiper text
        for c in self.chiper_text:
            # change c to num
            for k, v in self.all_character.items():
                if k == c:
                    num = int(math.pow(v, self.private_lock[0])%self.private_lock[1])
                    decrypted_list.append(num)
        
        for de in decrypted_list:
            for k, v in self.all_character.items():
                if de == v:
                    decrypted_text+=k
        print('-'*10)
        print('hasil dekripsi = ',decrypted_text)
        print('-'*10)




if __name__ == '__main__':
    rsa = Rsa()
    text = str(input('Type the text : '))
    rsa.encrypt_text(text)
    rsa.decrypt_text()