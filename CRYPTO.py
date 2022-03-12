from sympy import isprime
import random


def string_to_int(string):
    output = ['1']
    for char in string:
        unicodedstr = str(ord(char))
        unicodedoutput = []
        for i in range(3):
            index = len(unicodedstr)-i-1
            if index >= 0:
                unicodedoutput.insert(0, unicodedstr[index])
            else:
                unicodedoutput.insert(0, '0')
        output.extend(unicodedoutput)
    return int(''.join(output))


def int_to_string(num):
    string = str(num)[1:]
    output = []
    for i in range(0, len(string), 3):
        output.append(chr(int(string[i:i+3])))
    return ''.join(output)


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


start, end = pow(10, 200), pow(10, 300)


class RSA:
    def __init__(self, keys=None):
        if not keys:
            prime1 = 0
            while not isprime(prime1):
                prime1 = self.rand()
            prime2 = 0
            while not isprime(prime2):
                prime2 = self.rand()
            self.mod = prime1*prime2
            coprime = (prime1-1)*(prime2-1)
            coprimes = reversed(range(2, coprime))
            for e in coprimes:
                if is_coprime(e, coprime) and is_coprime(e, self.mod):
                    self.pub = e
                    break
            self.priv = (self.rand()*coprime)-1
            self.priv = hex(self.priv)
            self.pub = hex(self.pub)
            self.mod = hex(self.mod)
            return

        if 'pub' in keys:
            self.pub = keys['pub']
        else:
            self.pub = None
        if 'priv' in keys:
            self.priv = keys['priv']
        else:
            self.priv = None
        self.mod = keys['mod']

    def rand(self): return random.randint(start, end)

    def encrypt(self, num):
        return hex(pow(num, int(self.pub, 0), int(self.mod, 0)))

    def decrypt(self, num):
        return pow(int(num, 0), int(self.priv, 0), int(self.mod, 0))

    def encrypt_str(self, string):
        return self.encrypt(string_to_int(string))

    def decrypt_to_str(self, hex):
        return int_to_string(self.decrypt(hex))

    def __str__(self):
        return f'PUBLIC:\n{self.pub}\nPRIVATE:\n{self.pub}\nMODULOS:\n{self.mod}'

    def toObj(self):
        output = {}
        if self.priv:
            output['priv'] = self.priv
        if self.pub:
            output['pub'] = self.pub
        output['mod'] = self.mod
        return output


while True:
    choose = int(input('1) make keys\n2) encrypt\n3) decrypt\n\nchoose: '))
    if choose == 1:
        crypto = RSA()
        print('keys:')
        print('\nprivate key (DON\'T GIVE AWAY!):', crypto.priv)
        print('\npublic key (anyone can have this):', crypto.pub)
        print('\nmod (anyone can have this):', crypto.mod)
    elif choose == 2:
        crypto = RSA(
            {
                'pub': input('\npublic key: '),
                'mod': input('\nmod: ')
            }
        )
        message = input('\nmessage: ')
        print('\nencrypted:', crypto.encrypt_str(message))
    else:
        crypto = RSA(
            {
                'priv': input('\nprivate key: '),
                'mod': input('\nmod: ')
            }
        )
        encrypted = input('\nencrypted: ')
        print('\ndecrypted:', crypto.decrypt_to_str(encrypted))
    print()
