from CRYPTO import RSA

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
