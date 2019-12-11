def toCelsius(farenheit = int(input("Podaj temperature w stopniach Farenheita\n"))):
    celsius = (farenheit-32)*5/9
    return celsius

print(toCelsius())