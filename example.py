from RSA import RSA
import json

choose = int(input('1) make keys\n2) encrypt\n3) decrypt\n\nchoose: '))
if choose == 1:
    crypto = RSA()
    json.dump(crypto.toObj(), open('keys.json', 'w'))
    print('saved to keys.json')
else:
    crypto = RSA(
        json.load(open('keys.json', 'r'))
    )
    if choose == 2:
        message = input('message: ')
        print('encrypted:', crypto.encrypt_str(message))
    else:
        encrypted = input('encrypted: ')
        print('decrypted:', crypto.decrypt_to_str(encrypted))
