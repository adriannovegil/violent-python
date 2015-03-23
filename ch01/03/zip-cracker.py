import zipfile
import optparse
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
	# Definimos el mensaje de ayuda.
	parser = optparse.OptionParser("usage %prog " + "-f <zipfile> -d <dictionary>")
	# Definimos el parametro -f, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-f', dest='zname', type='string', help='specify the zip file')
	# Definimos el parametro -d, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	# Parseamos los datos de entrada.
	(options, args) = parser.parse_args()
	# Si el usuario no ha especificado el nombre del ficheo O el fichero de diccionario
	# terminamos mostrando el mensaje de uso del comando.
	# En caso contrario, recuperamos los valores de los parametros.
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit(0)
	else:		
		zname = options.zname
		dname = options.dname
	# Abrimos el fichero a crackear
	zFile = zipfile.ZipFile(zname)
	# Abrimos el fichero que contiene el diccionario.
	passFile = open(dname)
	## Comenzamos con la tarea de crackear el password.
	for line in passFile.readlines():
		password = line.strip('\n')
		# Creamos un nuevo thread. Le indicamos la funcion a jecutar y los parametros de
		# entrada de la misma.
		t = Thread(target=extractFile, args=(zFile, password))
		# Ejecutamos el thread.
		t.start()

if __name__ == '__main__':
	main()	