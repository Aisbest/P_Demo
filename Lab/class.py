class person:
    def __init__(self , init_name):
        self.name = init_name
    def greet(self):
        print("my name is :" + self.name)

p1 = person("devid")
p1.greet()