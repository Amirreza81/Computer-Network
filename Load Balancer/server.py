import socket
import threading
import time


def check_servers(server):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server)
    client_socket.send("checking".encode())

    response = client_socket.recv(1024).decode()
    client_socket.close()

    if response == "Yes":
        return True
    return False


class LoadBalancer:
    def __init__(self):
        self.all_of_servers = []
        self.available_servers = []
        # dict for counting number of each time we work on each server
        self.counters = {}
        self.current_index = 0
        self.ip = '127.0.0.1'

    def get_next_server_rr(self):
        server = self.available_servers[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.available_servers)
        return server

    def loading(self):
        with open('config', 'r') as file:
            for line in file:
                ip_addr, port = line.strip().split()
                self.all_of_servers.append((ip_addr, int(port)))
        for server in self.all_of_servers:
            self.available_servers.append(server)
        self.counters = {server: 0 for server in self.available_servers}

    def check_servers_part(self):
        while True:
            time.sleep(60)
            available_servers = []
            for server in self.all_of_servers:
                if check_servers(server):
                    available_servers.append(server)
            self.available_servers = available_servers

    def start(self):
        threading.Thread(target=self.check_servers_part, daemon=True).start()
        # host = socket.gethostname()
        host = self.ip
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # _, port = server_socket.getsockname()
        server_socket.bind((host, 1000))
        server_socket.listen()
        print("Server with load balancer is ready...")
        i = 0
        while True:
            i += 1
            conn, addr = server_socket.accept()
            server = self.get_next_server_rr()
            self.counters[server] += 1
            print("######################################")
            print(f"Request from {addr}")
            print(f"Forwarding to {server}")
            print("######################################")

            conn.send((server[0] + "," + str(server[1])).encode())
            conn.close()
            if i % 50 == 0:
                requests = sum(self.counters.values())
                infoss = {}
                for server, request_count in self.counters.items():
                    infoss[server] = (request_count / requests) * 100
                print(infoss)


def main():
    load_balancer = LoadBalancer()
    load_balancer.loading()
    load_balancer.start()


main()
