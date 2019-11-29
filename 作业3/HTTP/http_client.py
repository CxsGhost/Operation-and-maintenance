from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return ["Hello,Python!不用写底层代码真是太好了，你太强了".encode("gbk")]
    # 这个地方用utf-8汉字竟然是乱码。。


my_http = make_server("", 8000, application)
print("服务器正在运行，端口：8000")
my_http.serve_forever()