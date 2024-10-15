import socket

def udp_client():
    SERVER = '127.0.0.1'
    PORT = 8888
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    dest = (SERVER, PORT)

    print("Calculadora UDP - Digite 'encerra' para finalizar")
    while True:
        operation = input("Digite a operação (soma, subtracao, multiplicacao, divisao, raiz, encerra): ")
        if operation == 'encerra':
            udp.sendto(operation.encode(), dest)
            break
        
        op1 = input("Digite o primeiro operando: ")
        op2 = input("Digite o segundo operando (se aplicável): ")
        
        message = f"{operation} {op1} {op2}"
        udp.sendto(message.encode(), dest)
        
        result, _ = udp.recvfrom(1024)
        print("Resultado:", result.decode())

    udp.close()

if __name__ == '__main__':
    udp_client()
