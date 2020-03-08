def zad1():
    print('''
 BIN | DEC | HEX
-----+-----+-----
''', end='')
    for i in range(0b10000):
        print(f' {i:04b}|   {i:2}|   {i:x}')

def zad2():
    print('''
           BIN          |   DEC  | HEX
------------------------+--------+------
''', end='')
    for i in [0b101, 7, 24, 0xff, 1000, 128, 0xa8f, 512, 101010, 0xb2ea, 0b111111, 0xfff, 1023, 0xffffff, 0b1111111111]:
        print(f'{i:024b}|{i:8}|{i:06x}')
zad1()
zad2()