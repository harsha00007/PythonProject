# class MyClass:
#     def __init__(self, name="h", age=21):
#         self.name = name
#         self.age = age
#     def details(self):
#         print(self.name, self.age)
# m = MyClass()
# m1 = MyClass("harsha", 22)
# m.details()
# m1.details()
# print(m.name, m.age)


class MyClass:
    def __init__(self):
        self.__name = "harsha"
        self.__age = 21
    def details(self):
        print(self.__name, self.__age)
    def set(self, age):
        self.__age = age
m = MyClass()
m.set(22)
m.details()

# print(int("xyz"))

