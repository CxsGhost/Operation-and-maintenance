import socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 6666
    addr = (host, port)

    sock.connect(addr)
    print("连接服务端成功")
    txt = sock.send(input('想要发送的内容：').encode("utf-8"))
    byte = sock.recv(1024).decode("utf-8")
    print(byte)
    sock.close()
except Exception as e:
    print(e)

