import socket
import ssl

data_file = open("bilibil.txt", "w")
url = "www.bilibili.com"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = ssl.wrap_socket(s)
addr = (url, 443)

# 尝试连接服务器
try:
    client.connect(addr)
    print("连接成功！")
    client.send("""GET /?rt=V%2FymTlOu4ow%2Fy4xxNWPUZ2xTp5JRBCpn0cKuM1JH7O0%3D/ \
    HTTP/1.1\r\nHost: www.bilibili.com\r\nUser-Agent: Mozilla/5.0 (Windows NT 10.0; \
    Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/78.0.3904.108 Safari/537.36\r\n\r\n""".encode("utf-8"))
except Exception as e:
    print("连接失败！\n {}".format(e))

# 开始接收数据
while True:
    response = client.recv(4096)
    if not len(response):
        print("数据接收完毕！")
        break
    print("数据保存中...")
    data = response.decode("utf-8")  # 尝试过gbk发现更不行。。。
    data_file.write(data)
    print(data)
data_file.close()
client.close()
