import crypt

# Funcion que se encarga de romper el password. Como parametros le pasamos
# uno de los password que hemos extraido del fichero de passwords. La funcion
# se encarga de recorrer el fichero de diccionario, cifrar cada uno de los password
# y compararlo con el original para ver si hay coincidencia.
def testPass(cryptPass):
	salt = cryptPass[0:2]
	# Fichero de diccionario.
	dictFile = open('dictionary.txt','r')
	# Recorresmos las palabras del fichero de diccionario. Cifraremos y compararamos
	# cada una de las palabras.
	for word in dictFile.readlines():
		word = word.strip('\n')
		# Ciframos la palabra.
		cryptWord = crypt.crypt(word,salt)
		# Comparamos el password original con la palabra cifrada para ver si hay
		# coincidencia.
		if (cryptWord == cryptPass):
			print "[+] Found Password: "+ word + "\n"
			return
	print "[-] Password Not Found.\n"
	return

# Funcion principal.
def main():
	# Fichero que contiene los password que queremos romper.
	passFile = open('passwords.txt')
	# Leemos las lineas del fichero de passwords.
	for line in passFile.readlines():
		if 	":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password For: " + user
			testPass(cryptPass)

# Arrancamos!!!
if __name__ == "__main__":
	main()