class number:
    def __init__(self, v):
        self.value = v

    def double(self):
        return self.value * 2

    def sqrt(self):
        return (self.value) ** 0.5


num = number(2)
print(num.double())
print(num.sqrt())