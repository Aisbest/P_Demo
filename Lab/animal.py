class Animal():
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("my name is: "+self.name)

class Dog(Animal):
    def greet(self):
        print("wangwang, my name is:"+self.name)

class Cat(Animal):
    def greet(self):
        print("miaomiao, my name is:"+self.name)