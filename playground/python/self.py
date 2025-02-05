class MyClass:
    def __init__(self, value):
        self.value = value  # 'self.value' refers to the instance variable 'value'

    def display_value(self):
        print(self.value)  # 'self.value' accesses the instance variable 'value'

    def increment_value(self):
        self.value += 1  # 'self.value' accesses the instance variable 'value'
        self.display_value()  # 'self.display_value()' calls another instance method

# Create an instance of MyClass
obj = MyClass(10)
obj.increment_value()  # Output: 11
