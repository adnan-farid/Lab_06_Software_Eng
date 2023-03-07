#adnan farid
#func that encodes pw
def encode(pwd):
    #empty list
    pwd_lst = []
    #string is divided into list
    pwd_lst[:] = pwd
    new_pwd = ''
    #loops through list, adds three to each digit, and defines a new string
    for i in range(len(pwd_lst)):
        pwd_lst[i] = str(int(pwd_lst[i]) + 3)
        new_pwd += pwd_lst[i]
    #returns encoded string
    return new_pwd
def decode(pwd):
    pass




#main method
def main():
    program_init = True
    #loops through the program until user exits
    while program_init == True:
        print('Menu')
        print('------------- ')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('\n')
        user_op = int(input('Please enter an option: '))
        #option 1 calls encode function and stores encoded pwd
        if user_op == 1:
            pwd = str(input('Please enter your password to encode: '))
            new_pwd = encode(pwd)
            print('Your password has been encoded and stored!')
            print('\n')
        # prints encoded pwd and decoded pwd
        if user_op == 2:
            pass
        #exits program
        if user_op == 3:
            program_init = False






if __name__ == '__main__':
    main()
