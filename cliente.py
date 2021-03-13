import socket

host = '127.0.0.1' #mesmo local
porta = 8800 #mesma porta

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host, porta)
soquete.connect(envio)

print('Digite: S e pressione enter para encerrar....')
print('DIGITE A MENSAGEM: ')
mensagem = input()

while mensagem not in ('s', 'S'):#um loop com while sob a condição de enquanto não digitado a letra s ou S pelo cliente,
    soquete.send(str(mensagem).encode()) ## as mensagens serão enviadas ao servidor através da função send
    mensagem = input()
soquete.close()