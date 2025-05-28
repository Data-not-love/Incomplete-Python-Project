class Person:
    # class varialbe
    count = 0

    #constructor
    def __init__ (self,name,age):
        self.__name = name
        self.__age = age
        Person.increment_count()

    # class
    @classmethod
    def increment_count(cls):
        cls.count = cls.count + 1
    # instance
    def greeting(self):
        print("Hello")
    # static
    @staticmethod
    def cls_information():
        print("the information of class:")
        print(f" class name: {Person.__name__}")
        print(f" class name: {Person.__bases__}")
        print(f" the number of object created: {Person.count}")
    # instance
    def __str__(self):
        return f'My name is {self.__name}. I am {self.__age} years old'
han = Person('han',23)
han.greeting()
han.cls_information()