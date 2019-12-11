print("Tekst który chcesz zaszyfrować zapisz w pliku translate.txt, możesz go też utworzyć tutaj, czy chcesz to zrobić?")
while 1:
    choice = input("Jeżeli chcesz to podaj znak T, jeżeli nie to podaj znak N\n")
    if choice == 'T':
        newFile = open('translate.txt', 'w')
        newFile.write(input("Podaj tekst jaki chcesz zapisać w pliku. Bez polskich znaków\n"))
        newFile.close()
        break
    if choice == 'N':
        break
change = int(input("Podaj o ile liter chcesz przeskoczyć\n"))
to_translate = open('translate.txt', 'r')
to_translate_text = to_translate.read()
to_translate.close()
translated_text = None
for letter in to_translate_text:
    if letter == ' ':
        translated_text += ' '
        continue
    trans = ord(letter) + change
    if ord(letter) < 123 and ord(letter) > 96:
        if trans > 122:
            trans -= 26
    if ord(letter) < 91 and ord(letter) > 64:
        if trans > 90:
            trans -= 26
    if translated_text == None:
        translated_text = chr(trans)
    else:
        translated_text += chr(trans)
finalFile = open('result.txt', 'w')
finalFile.write(translated_text)
finalFile.close()
print("Wynik jest w pliku result.txt")