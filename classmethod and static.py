class MyClass:
    var = "class_variable_value"

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def class_method(cls):
        print("Class method called")
        print("Accessing class variable:", cls.var)

    @staticmethod
    def static_method():
        print("Static method called")

# Create an instance of MyClass
obj = MyClass("instance_variable_value")

# Calling the class method

MyClass.class_method()

# Calling the static method
MyClass.static_method()
