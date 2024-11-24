import socket
from .interpreter import Interpreter
from .interpreter import Parser
def start_server(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.bind((host,port))
        sock.listen(2)

        while True:
            print("Wait fo new connection...")
            conn,addr=sock.accept()
            print(f"Connection {addr}")
            while True:
                message=conn.recv(1024)
                if message==b"exit" or message==b"":
                    conn.send(b"goodbye")
                    break
                try:
                    if message.startswith(b"@"):
                        parser=Parser()
                        result=parser.eval(message.decode()[1:])
                    else:
                        interp=Interpreter()
                        result=interp.eval(message.decode())
                    conn.send(str(result).encode())
                except (SyntaxError,RuntimeError) as e:
                    conn.send(("error:"+str(e)).encode())
