class Pet(object):
    def __init__(self,name,group,age):
       self.name = name
       self.group = group
       self.age = age

    def get_old(self):
        self.age = self.age + 1

    def greet(self, other):
        print("Hello", other.name)