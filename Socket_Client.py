import socket


class Client:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.s = None

    def connect(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.settimeout(0.02)
            self.s.connect((self.ip, self.port))
        except socket.error:
            print "No connection to server {}/{} possible..".format(self.ip, self.port)

    def send_string(self, data):
        try:
            to_send = str(data) + "\n"
            self.s.sendall(to_send)
            # print "Sent: {}".format(data)
        except socket.error:
            print "No connection to server {}/{}. Attempting to reconnect..".format(self.ip, self.port)
            self.connect()

    def close_socket_conn(self):
        self.s.shutdown(socket.SHUT_WR)
        self.s.close()
