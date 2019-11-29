from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, Python</h1>'
    return [body.encode('utf-8')]


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('127.0.0.1', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
