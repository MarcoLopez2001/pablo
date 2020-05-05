def sin_vocales(text):
	vocales = ['a','A','e','E','i','I','o','O','u','U']
	res = ''
	for letter in text:
		if letter not in vocales and letter != " ":
			res += letter
			
	return res

x = str(input("Ingrese una palabra: "))
print("Texto:", x)
print(len(sin_vocales(x)),"consonantes")
