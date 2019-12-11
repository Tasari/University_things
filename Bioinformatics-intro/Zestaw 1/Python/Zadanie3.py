def silnia(a):
    if a == 0:
        return 1
    else:
        return a*silnia(a-1)

for repeat in range(1,11):
    print("{}! = ".format(repeat), silnia(repeat))