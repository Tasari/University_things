text = input("Podaj tekst\n")
words = text.split()
letters = 0
for word in words:
	for letter in word:
		letters += 1
print("Twoj tekst zawiera {} wyrazow, i w sumie {} liter nie liczac spacji, z tego wynika, że na wyraz przypada {} słów.".format(len(words), letters, letters/len(words)))