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

def tcp_server():
    HOST = ''
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind((HOST, PORT))
    tcp.listen(1)
    
    print("Servidor TCP pronto para receber mensagens na porta", PORT)
    
    while True:
        con, client = tcp.accept()
        print(f"Conectado por {client}")
        msg = con.recv(1024).decode()

        if msg.lower() == 'encerra':
            print("Encerrando servidor TCP...")
            con.send(b"Servidor encerrado")
            break
        
        # Desempacotamento da mensagem
        parts = msg.split()
        operation = parts[0]
        op1 = parts[1] if len(parts) > 1 else None
        op2 = parts[2] if len(parts) > 2 else None

        result = process_operation(operation, op1, op2)
        con.send(result.encode())

    tcp.close()

if __name__ == '__main__':
    tcp_server()
