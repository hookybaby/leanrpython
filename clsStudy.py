#_*_ coding:utf-8 _*_


class parent:
    def __init__(self):
        print("parent init method")

    def showmessage(self):
        print("showmessage")

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroy")


cls = parent()

cls.showmessage()