import socket
import get  # 自己写的
import threading
import os


class ChatSever:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get.get_ip(), 10000)
        self.users = {}

    @property
    def start_sever(self):
        self.sock.bind(self.addr)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")

        threading.Thread(target=self.accept_cont).start()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(addr, number))

            threading.Thread(target=self.recv_send, args=(s, addr)).start()
            # threading.Thread(target=self.send_msg, args=(s, addr)).start()

    def recv_send(self, sock, addr):
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("gbk")
                msg = "{}用户{}发来消息：{}".format(get.get_time(), addr, response)

                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(addr))
                self.users.pop(addr)
                break

    @property
    def stop_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever = ChatSever()
    while True:
        cmd = input(">>>")
        """
        只有服务器管理员知晓正确的命令
        由此开启和关闭服务
        """
        try:
            exec("sever."+cmd)
        except Exception as e:
            print("输入命令无效，请重新输入！")
            print(e)
