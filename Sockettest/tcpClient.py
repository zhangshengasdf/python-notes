#!/usr/bin/python3
# coding=utf-8


import socket

if __name__ == '__main__':

    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_client_socket.connect(("192.168.1.123", 8080))

    send_data = "你好服务段，这是客户端！".encode()

    tcp_client_socket.send(send_data)

    recv_data = tcp_client_socket.recv(1024)

    print(recv_data)

    recv_content = recv_data.decode()

    print("接收服务段：", recv_content)

    tcp_client_socket.close()
