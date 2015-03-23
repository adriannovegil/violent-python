import 	zipfile

# Funcion que valida si el password es necesario para el fichero.
def extractFile(zFile, password):
	try:
		zFile.extractall(pwd=password)
		return password;
	except:
		return

# Funcion principal. Recorre el fichero de diccionario y prueba claves
# para ver si son la adecuada.
def main():
	zFile = zipfile.ZipFile("evil.zip")
	passFile = open('dictionary.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		guess = extractFile(zFile, password)
		if guess:
			print '[+] Password = ' + password + '\n'
			exit(0)

if __name__ == '__main__':
	main()	