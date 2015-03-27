import optparse
from socket import *

# Funcionq ue lleva a cabo una conexion a una ip y puerto que le pasamos como
# parametro.
def connScan (tgtHost, tgtPort):
	try:
		# Creamos un socker.
		connSkt = socket(AF_INET, SOCK_STREAM)
		# nos conectamos usando la isntancia de socket que hemos creado.
		connSkt.connect((tgtHost, tgtPort))
		# Enviamos un stream con datos de prueba para verificar si hay
		# respuesta.
		connSkt.send('ViolentPython\r\n')
		# Recogemos la respuesta al servicio.
		results = connSkt.recv(100)
		# Mostramos el resultado de la conexion
		print '[+] %d/tcp open'% tgtPort
		print '[+] ' + str(results)
		# Cerramos el socket.
		connSkt.close()
	except:
		# En caso de error en la conexion con el servicio.
		print '[-]%d/tcp closed'% tgtPort

# Funcion que se encarga del escaneado de puertos para la ip dada.
def portScan (tgtHost, tgtPorts):
	try:
		tgtIp = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host " % tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIp)
		print '\n[+] Scan Results for: ' + tgtName[0]
	except:
		print '\n[+] Scan Results for: ' + tgtIp
	setdefaulttimeout(1)
	# Para cada uno de los puertos, realizamos una conexion para verificar
	# si existe algun servicio a la escucha o no.
	for tgtPort in tgtPorts:
		print '[+] Scanning port ' + tgtPort
		connScan(tgtHost, int(tgtPort))

# Funcion principal.
def main():
	# Mensaje de uso del comando.
	parser = optparse.OptionParser('Usage %prog -H <target host> -p <target port>')
	# Comandos del comando.
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target port[s] separated by comma')	
	# Parseamos los parametros.
	(options, args) = parser.parse_args()
	# Recuperamos la ip del equipo a escanear
	tgtHost = options.tgtHost
	# Recuperamos la lista de puerdos. Hacemos un split por coma.
	tgtPorts = str(options.tgtPort).split(',')
	# Si los parametros son correctos, procedemos con el escaneo, en caso 
	# contrario, mostramos un error y el uso del comando.
	if (tgtHost == None) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and port[s].'
		exit(0)
	# Lazamos el escaneo de puertos.
	portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
	main()