option = 1
while option != 'K':
    option = input('''
A - ...
B - ...
C - ...
D - ...
K - END
''').upper()
    if option in ['A', 'B', 'C', 'D', 'K']:
        print(f'wybrano {option}')
    else:
        print('bad data')


