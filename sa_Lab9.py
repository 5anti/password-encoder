#
# Santiago Alvarez
#
# April 10, 2024
#


def encode(unencoded_password):
    encoded_password = ""
    for char in unencoded_password:
        old_digit = int(char)
        new_digit = (int(char) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_passwd):
    """Decodes password by shifting numbers
    3 times back"""

    passwd = ''

    for num in encoded_passwd:
        num = int(num)
        new_num = (num - 3) % 10
        passwd += str(new_num)

    return passwd


def main():
    menu = '''
    Password Encoder/Decoder
    ------------------------
    1. Encode password
    2. Decode password
    3. Exit
    '''
    print(menu)

    while True:
        option = str(input('\n>> What would you like to do? '))

        # Option 1: Encode password
        if option == '1':
            passwd = str(input('> Input password to encode: '))
            result = encode(passwd)
            print('[+] Encoded password: {}\n'.format(result))

            pass

        # Option 2: Decode password
        elif option == '2':
            passwd = str(input('> Input password to decode: '))
            result = decode(passwd)
            print('[+] Decoded password: {}'.format(result))

        elif option == '3':
            break

        else:
            print('[!] ERROR: Option not recognized.')


if __name__ == '__main__':
    main()
