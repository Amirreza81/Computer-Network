# AmirReza Azari 99101087

import sys
import random
import socket
import threading

host = '127.0.0.1'


# print("Host name: ", socket.gethostname())


def starting(host1, port1, d):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host1, port1))
    server_socket.listen()

    while True:
        conn, addr = server_socket.accept()
        mess = conn.recv(1024).decode()

        if mess == "checking":  # from server.py
            rand = random.random()
            strr = "No" if rand < 0.15 else "Yes"
            conn.send(strr.encode())

        if mess == "Start":  # from hw2.py
            conn.send(("##### \nServer ID: " + str(d) + ", Port: " + str(port1) +
                       ", IP: " + str(host1) + " #####\n").encode())

        conn.close()


def main():
    argss = sys.argv
    instance_number = int(argss[1])  # numbers of servers
    print("It’s instance number ", instance_number)
    f = open("config", "w")

    for j in range(instance_number):
        port = random.choice(list(range(1001, 9999)))
        server_id = j + 1
        f.write(str(host) + " " + str(port) + "\n")
        threading.Thread(target=starting, args=(host, port, server_id,)).start()
    f.close()


main()
