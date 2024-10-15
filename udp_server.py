import socket
import math

def process_operation(operation, op1, op2=None):
    try:
        op1 = float(op1)
        if op2 is not None:
            op2 = float(op2)
        
        if operation == 'soma':
            return str(op1 + op2)
        elif operation == 'subtracao':
            return str(op1 - op2)
        elif operation == 'multiplicacao':
            return str(op1 * op2)
        elif operation == 'divisao':
            if op2 == 0:
                return "Erro: divisão por zero"
            return str(op1 / op2)
        elif operation == 'raiz':
            if op1 < 0:
                return "Erro: raiz quadrada de número negativo"
            return str(math.sqrt(op1))
        elif operation == 'encerra':
            return "ENCERRAR"
        else:
            return "Erro: operação desconhecida"
    except ValueError:
        return "Erro: operandos não numéricos"

def udp_server():
    HOST = ''  # Escuta em qualquer IP
    PORT = 8888  # Porta do servidor
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind((HOST, PORT))
    
    print("Servidor UDP pronto para receber mensagens na porta", PORT)
    
    while True:
        # Recebendo dados do cliente
        msg, client_address = udp.recvfrom(1024)
        msg_decoded = msg.decode()
        
        if msg_decoded.lower() == 'encerra':
            print("Encerrando servidor UDP...")
            udp.sendto(b"Servidor encerrado", client_address)
            break
        
        # Desempacotamento da mensagem
        parts = msg_decoded.split()
        operation = parts[0]
        op1 = parts[1] if len(parts) > 1 else None
        op2 = parts[2] if len(parts) > 2 else None

        # Processando a operação
        result = process_operation(operation, op1, op2)
        udp.sendto(result.encode(), client_address)
    
    udp.close()

if __name__ == '__main__':
    udp_server()
