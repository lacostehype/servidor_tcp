import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind(("127.0.0.1", 4433))
    servidor.listen(10)
    print ("Servidor Online!")
    cliente, endereco = servidor.accept()
    print ("Conexão Recebida de:" + endereco[0])
    while True:
        data = cliente.recv(9999).decode()
        print (data)
        cliente.send(input("Mensagem:").encode())
    servidor.close()
except Exception as erro:
    print ("ERRO >>>", erro)
    servidor.close()
