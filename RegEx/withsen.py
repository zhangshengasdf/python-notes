#!/usr/bin/python3
# coding=utf-8


class File(object):
    def __init__(self, file_name, file_model):
        self.file_name = file_name
        self.file_model = file_model

    def __enter__(self):
        print("进入上文方法")
        self.file = open(self.file_name, self.file_model)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("进入下文方法")
        self.file.close()

if __name__ == '__main__':
    with File("1.txt", "r") as file:
        file_data = file.read()
        print(file_data)

