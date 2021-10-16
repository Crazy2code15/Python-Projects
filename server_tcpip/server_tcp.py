#coding:utf-8
from socket import *
import sys
import os

#função

def extension(archive):
	ext = ''
	if (archive == '.txt'):
		ext = 'Content-Type: text/plain\r\n'
	elif (archive == '.png'):
		ext = 'Content-Type: image/png\r\n'
	elif (archive == '.html'):
		ext = 'Content-Type: text/html\r\n'

	return ext

door = 8000
socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('', door))
socket.listen(1)

print ('http://localhost:{}/'.format(door) + 'is received...')


while True:
	connection, address = socket.accept()
	linner =connection.recv(1024).decode('utf-8').split(' ')
	method = linner[0]
	path = linner[1]
	version = linner[2].split('\r\n')[0]
	head = ''

	try:
		if (path == '/'):
			path = '/index.html'


		archive = open('.' + path, 'rb')
		leitura = archive.read()
		archive.close()
		head = '{} 200 OK\r\n'.format(version)
		name, archive = os.path.splitext(path)
		ext = extension(archive)
		head += ext

		package_send = head.encode('utf-8') + '\r\n'.encode('utf-8') + leitura + "\r\n".encode('utf-8')
		print('{} {} - {} 200 OK'.format(method, path, name))
		connection.send(package_send)


	except:


		head = '{} 404 NOT FOUND\r\n'.format(version)
		print('{} {} - 404 NOT FOUND'.format(method, path))
		error = 'Archive ' + path + ' not found.'
		connection.send(error.encode('utf-8'))


	connection.close()

