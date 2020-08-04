#!/usr/bin/python3
# coding=utf-8


import socket
import threading

def handle_client_request(service_client_socket, ip_port):
    while True:
        recv_data = service_client_socket.recv(1024)

        if recv_data:
            print(recv_data.decode(), ip_port)

            service_client_socket.send("ok, 问题正在处理中...".encode())
        else:
            print("客户端下线了：", ip_port)
            break
    service_client_socket.close()


if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 8080))
    tcp_server_socket.listen(128)

    while True:
        service_client_socket, ip_port = tcp_server_socket.accept()
        print("客户端连接成功：",ip_port)

        sub_thread = threading.Thread(target = handle_client_request, args = (service_client_socket, ip_port))
        sub_thread.setDaemon(True)

        sub_thread.start()

    tcp_server_socket.close()

