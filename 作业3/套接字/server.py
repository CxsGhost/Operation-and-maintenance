import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 6666
addr = (host, port)

server.bind(addr)

server.listen(1)

print("等待客户端连接....")
client, addr = server.accept()
print("连接成功")
txt = client.recv(1024)
print("接收到客户端发送的信息:{}".format(txt.decode("utf-8")))
client.send(txt)
client.close()
