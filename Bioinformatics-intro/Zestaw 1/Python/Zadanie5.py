given_thing = input("Podaj cokolwiek aby wyświetlić to w odwrotnej kolejności\n")
print(given_thing)
length = len(given_thing)
reverse = None
while length > 0:
    if reverse == None:
        reverse = given_thing[length - 1]
    else:
        reverse = reverse + given_thing[length - 1]
    length -= 1
print(reverse)