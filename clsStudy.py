#_*_ coding:utf-8 _*_


class parent:
    __privateName="Josh" # 私有变量
    def __init__(self):
        print("parent init method")

    def showmessage(self):
        print("showmessage")

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroy")
        print(self.__privateName)


cls = parent()

cls.showmessage()