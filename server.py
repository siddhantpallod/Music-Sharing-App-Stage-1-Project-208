import socket
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients = {}

def acceptConnections():
    global SERVER
    global clients
    
    while True:
        client, addr = SERVER.accept()
        client_name = client.recv(4096).decode().lower()
        
        print(f"Connection established with {client_name} : {addr}")
        
def setup():
    print("\n\t\t\t\t\t Music Sharing App\n")
    
    global PORT
    global IP_ADDRESS
    global SERVER
    
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))
    
    SERVER.listen(100)
    
    print('\t\t\t\t SERVER IS WAITING FOR INCOMING CONNECTIONS...')
    
    acceptConnections()

setup_thread = Thread(target = setup)
setup_thread.start()