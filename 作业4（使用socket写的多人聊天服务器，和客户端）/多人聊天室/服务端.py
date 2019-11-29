import socket
import threading
import os
import get  # 这个包是自己写的

addr = (get.get_ip(), 10000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)
print("正在等待连接....\n")
sever, addr_s = s.accept()


def recv_msg():
    print("连接成功！现在可以接收消息！\n")
    while True:  # 这里发现另一端在send_msg中关闭套接字后会报错。。。于是用try捕获报错信息并正常退出
        try:
            response = sever.recv(1024)
            recv_time = get.get_time()
            print("{} 接收到信息:{}".format(recv_time, response.decode("gbk")))
        except ConnectionResetError:
            print("对方已经退出聊天")
            s.close()
            break
    os._exit(0)


def send_msg():
    print("连接成功！现在可以发送消息！\n")
    print("输入消息按回车来发送")
    print("输入esc来退出聊天")
    while True:
        msg = input()
        if msg == "esc":
            print("退出聊天")
            s.close()
            break
        sever.send(msg.encode("gbk"))
    os._exit(0)


threads = [threading.Thread(target=recv_msg), threading.Thread(target=send_msg)]
for t in threads:
    t.start()
