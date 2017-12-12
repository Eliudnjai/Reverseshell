import socket
import sys

#create socket
def create_Socket():
    global host
    global port
    global s

    host="127.0.0.1"
    port=9999

    s=socket.socket()

#bind socket and try catch error
def bind_Socket():
    try:
        global port
        global host
        global s

        s.bind((host,port))
        s.listen(5)

        print("listening for connections...........")

    except socket.error as msg:
        print("Binding error "+str(msg) + '\n' + " retrying......")

        bind_Socket()

#accept connection from c->client
def accept_Conn():
    c,address=s.accept()

    print("Connection recv from " + " ip " + address[0] + " port " + str(address[1]))

    #include the send_commands function in accept_Conn
    send_commands(c)

    c.close()

def send_commands(c):
    while True:
        cmd=input()

        if cmd == 'quit':
            c.close()
            s.close()
            sys.exit()

        #send the cmd commands as str
        if len(str.encode(cmd)) > 0:
            c.send(str.encode(cmd))

            client_response=str(c.recv(1024),'utf-8')

            print(client_response,end='')

def main():
    create_Socket()
    bind_Socket()
    accept_Conn()
main()






