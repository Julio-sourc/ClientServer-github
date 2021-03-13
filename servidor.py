# criando um servidor e um cliente Python e trocando mensagens entre eles.
import socket
from datetime import *

host = '127.0.0.1' # o mesmo que local host
porta = 8800  #porta conexão

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #estou usando TCP/IP
recebe = (host, porta)
soquete.bind(recebe)
soquete.listen(2)

print('\nSERVIDOR INICIADO;......IP', host, 'PORTA', porta, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
while True:
    conexao, enderecoIP = soquete.accept()
    print('SERVIDOR ACESSADO PELO CLIENTE: ', enderecoIP, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print('\nIP CLIENTE: ', enderecoIP)
        print('MENSAGEM RECEBIDA: ', mensagem.decode())
    print('CONEXAO COM O CLIENTE FINALIZADA...', enderecoIP, 'EM: ',datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
    conexao.close()

