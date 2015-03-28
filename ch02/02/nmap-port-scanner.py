import nmap
import optparse

# Funcion que se encarga de llevar a cabo el escaneo de los pueros especificados
# como parametro, para la direccion ip indicada. Para llevar a cabo esta accion
# delegamos el trabajo duro en la libreria nmap.
def nmapScan(tgtHost, tgtPort):
	# Instancia de scaner nmap.
	nmScan = nmap.PortScanner()
	# Scaneamos el host que hemos indicado en el puerto indicado.
	nmScan.scan(tgtHost, tgtPort)
	# Podemos indexar el resultado del escaneo por ip y puerto.
	state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
	# Printeamos el resultado.
	print " [*] " + tgtHost + " tcp/"+tgtPort +" "+state

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
	for tgtPort in tgtPorts:
		nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
	main()