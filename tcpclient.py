from socket import *
serverName='localhost'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=raw_input('Input Lowercase sentence:')
clientSocket.send(sentence)
newSentence=clientSocket.recv(1024)
print newSentence
clientSocket.close()
