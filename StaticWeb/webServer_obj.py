#!/usr/bin/python3
# coding=utf-8


import socket
import threading


class HttpWebServer(object):
    def __init__(self):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 9000))
        tcp_server_socket.listen(128)

        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            new_socket.close()
            return

        recv_client_content = recv_client_data.decode()
        print(recv_client_content)

        request_list = recv_client_content.split(" ", maxsplit = 2)

        request_path = request_list[1]
        print(request_path)

        if request_path == "/":
            request_path = "/index.html"

        try:
            with open("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: PWS1.0\r\n"

            with open("static/error.html", "rb") as file:
                file_data = file.read()

            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            new_socket.send(response_data)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWS1.0\r\n"
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode() + response_body
            new_socket.send(response_data)
        finally:
            new_socket.close()

    def start(self):
        while(True):
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target = self.handle_client_request, args = (new_socket,))

            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    web_srever = HttpWebServer()
    web_srever.start()

if __name__ == '__main__':
    main()

            


