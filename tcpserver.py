from socket import *
serverPort=12000
serverSocket=socket(AF_INET	,SOCK_STREAM)
serverSocket.bind(('localhost',serverPort))
serverSocket.listen(1)
print 'server ready'
while 1:
	connectionSocket,addr=serverSocket.accept()
	sentence=connectionSocket.recv(1024)
	newSentence=sentence.upper()
	connectionSocket.send(newSentence)
	connectionSocket.close()		