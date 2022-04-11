import os
import re
import socket
from http import HTTPStatus


def get_open_port():
    with socket.socket() as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    srv_addr = ('', get_open_port())
    print(f'starting on {srv_addr}, pid: {os.getpid()}')

    s.bind(srv_addr)
    s.listen(1)
    conn, raddr = s.accept()

    while True:
        data = conn.recv(1024)
        text = data.decode('utf-8')
        if text:

            search_exp = '(POST|GET|PUT|DELETE|HEAD|CONNECT|OPTIONS|TRACE)'
            method = re.search(search_exp, text)

            code_id = text.find('/?status=') + 9
            try:
                code = int(text[code_id:code_id + 3])
                code = HTTPStatus(code).value
                code_name = HTTPStatus(code).name
            except ValueError:
                code = 200
                code_name = 'OK'

            status_line = f'HTTP/1.1 {code} {code_name}'
            request_method = f'Request Method: {method.group(1)}'
            request_source = f'Request Source: {raddr}'
            response_status = f'Response Status: {code} {code_name}'
            headers = text.split("\r\n\r\n")[0]

            body = '<b>' + request_method + '<br>' + '<b>' + request_source + '<br>' + '<b>' + response_status + '<br>'
            for item in headers.split('\n'):
                body += '<b>' + item + '<br>'

            headers = '\r\n'.join([
                status_line,
                headers
            ])

            resp = '\r\n\r\n'.join([
                headers,
                body
            ])
            sent_bytes = conn.send(resp.encode('utf-8'))
        else:
            conn.close()
            break
