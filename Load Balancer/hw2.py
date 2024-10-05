import socket
import threading
import time
import sys


def start_testing(load_balancer_addr):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(load_balancer_addr)
    server = client_socket.recv(1024).decode()
    client_socket.close()

    # print("server: ", server)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server.split(',')[0], int(server.split(',')[1])))
    client_socket.send("Start".encode())
    response = client_socket.recv(1024).decode()
    print(response)
    client_socket.close()


def main():
    argss = sys.argv
    host = '127.0.0.1'
    address = (host, 1000)
    num_requests = int(argss[1])
    for i in range(num_requests):
        thread = threading.Thread(target=start_testing, args=(address,))
        thread.start()
        time.sleep(0.1)


main()
