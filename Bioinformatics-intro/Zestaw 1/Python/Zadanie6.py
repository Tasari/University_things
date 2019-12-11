given_thing = input("Podaj znak, jeżeli podasz dłuższy ciąg zostanie sprawdzony tylko pierwszy element\n")
ascii_code = ord(given_thing[0])
if ascii_code >= 48 and ascii_code <= 57:
    print("Twój znak jest cyfrą")
elif ascii_code >= 65 and ascii_code <= 90:
    print("Twój znak jest wielką literą")
elif ascii_code >= 97 and ascii_code <= 122:
    print("Twój znak jest małą literą")
else:
    print("Twój znak to znak specjalny")