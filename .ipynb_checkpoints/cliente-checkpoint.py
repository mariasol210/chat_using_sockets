import threading
import sys
import socket
import pickle
import os

class Cliente():

    #es mejor usar puertos de 6 mil a 65 mil
	def __init__(self):
        
		valor = input("Dime la direccion que quieres usar: ")
		host = str (valor)
        
		valor = input("Dime el puerto que quieres usar: ")
		port = int (valor)
        
		print('Proceso con PID',os.getpid())
		print('Hilo PRINCIPAL con  ID:',threading.currentThread().getName())
		print('Hilo PRINCIPAL con  PID:',threading.currentThread().isDaemon())
		print('Hilos activos ahora mismo: ', threading.active_count())
   
		self.sock = socket.socket()
		self.sock.connect((str(host), int(port)))
		hilo_recv_mensaje = threading.Thread(target=self.recibir)
		hilo_recv_mensaje.daemon = True
		hilo_recv_mensaje.start()

		while True:
			msg = input('\nEscriba texto ? ** Enviar = ENTER ** Abandonar Chat = Q \n')
			if msg != 'Q' :
				self.enviar(msg)
			else:
				print(" **** TALOGOOO  ****")
				self.sock.close()
				sys.exit()

	def recibir(self):
		print('\t Hilo RECIBIR con ID:',threading.currentThread().getName())
		print('\t Pertenece al proceso con PID',os.getpid())
		print('\t Hilos activos ahora mismo: ', threading.active_count())
		while True:
			try:
				data = self.sock.recv(32)
				if data:
					print(pickle.loads(data))
			except:
				pass

	def enviar(self, msg):
		self.sock.send(pickle.dumps(msg))

c = Cliente()

		