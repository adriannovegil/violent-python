# Pxssh es un script especializado en ssh que esta incluido en la libreria
# pxssh. Incorpora las capacidades de dialogo directo con el servidor de ssh
# mediante funciones como login(), logout() o prompt()
import pxssh
import optparse
import os
from threading import *

maxConnections = 5
connection_lock = BoundedSemaphore(value = maxConnections)
Found = False
Fails = 0

# Funcion que se encarga de la conexion. Le pasamos como parametro los datos
# de acceso, usuario, host y password.
def connect(user, host, password, release):
	print 'Connect function'	

# Funcion principal.
def main():
	# Definimos el mensaje de ayuda
	parser = optparse.OptionParser('usage %prog -H ' + '<target host> -u <user> -d <directory>')
	# Definimos el parametro -H, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	# Definimos el parametro -d, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-d', dest='passDir', type='string', help='specify directory with keys')
	# Definimos el parametro -u, el nombre de la variable destino, el tipo (string) y el mensaje de ayuda.
	parser.add_option('-u', dest='user', type='string', help='specify the user')
	# Parseamos los datos de entrada.
	(options, args) = parser.parse_args()
	# Recuperamos los parametros de entrada
	host = options.tgtHost
	passDir = options.passDir
	user = options.user
	# Si alguno de los parametros no existe, mostramos el mensaje de uso del 
	# programa y salimos del mismo.
	if host == None or passDir == None or user == None:
		print parser.usage
		exit(0)

if __name__ == '__main__':
	main()