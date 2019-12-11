def fibonacci_chan(a):
    if a<3:
        return 1
    else:
        return fibonacci_chan(a-1) + fibonacci_chan(a-2)
print("Twój wynik to:\n" + str(fibonacci_chan(int(input("Podaj numer liczby której wartośc chcesz poznać\n")))))