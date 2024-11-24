import socket
def repl(host,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
        sock.connect((host,port))
        while True:
            print('in=',end="")
            text=input()
            if text=="exit" or len(text)==0:
                break
            sock.send(text.encode())
            answer=sock.recv(1024)
            print(f"out> {answer.decode()}")
        print("goodbye")