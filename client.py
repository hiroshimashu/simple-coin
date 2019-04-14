import socket 

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('192.168.3.6', 8000))
my_test = "Hello,This is test message from client"
my_socket.sendall(my_test.encode('utf-8'))
