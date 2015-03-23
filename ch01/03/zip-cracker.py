import 	zipfile
from threading import Thread, current_thread

# Funcion que valida si el password es necesario para el fichero.
def extractFile(zFile, password):
	print '[+] Thread : ' + str(current_thread().name) + ' testing password: ' + password
	try:
		zFile.extractall(pwd=password)
		print '[+] Found password: ' + password + '\n'		
	except:
		pass

# Funcion principal. Recorre el fichero de diccionario y prueba claves
# para ver si son la adecuada.
def main():
	zFile = zipfile.ZipFile("evil.zip")
	passFile = open('dictionary.txt')
	for line in passFile.readlines():
		password = line.strip('\n')
		t = Thread(target=extractFile, args=(zFile, password))
		t.start()

if __name__ == '__main__':
	main()	