import socket

def tcp_client():
    SERVER = '127.0.0.1'
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect((SERVER, PORT))

    print("Calculadora TCP - Digite 'encerra' para finalizar")
    while True:
        operation = input("Digite a operação (soma, subtracao, multiplicacao, divisao, raiz, encerra): ")
        if operation == 'encerra':
            tcp.send(operation.encode())
            break
        
        op1 = input("Digite o primeiro operando: ")
        op2 = input("Digite o segundo operando (se aplicável): ")

        message = f"{operation} {op1} {op2}"
        tcp.send(message.encode())

        result = tcp.recv(1024)
        print("Resultado:", result.decode())

    tcp.close()

if __name__ == '__main__':
    tcp_client()
