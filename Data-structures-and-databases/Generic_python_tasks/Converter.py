option = 1
while 1:
    option = input('''
b - bin
d - decimal
h - hex
k - END
''').lower()
    if option == 'b':
        i = int(input("Podaj liczbe\n"), base=2)
    elif option == 'h':
        i = int(input("Podaj liczbe\n"), base=16)
    elif option == 'd':
        i = int(input("Podaj liczbe\n"))
    elif option == 'k':
        break
    else:
        print('Error')
        continue
    print(f'{i:b}|{i}|{i:x}')