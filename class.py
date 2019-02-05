class math_1:
    mathematics = []

    def __init__(self):
        for i in self.mathematics:
            print(i *3)
    def subtraction(self):
        for i in self.mathematics:
            print(i - 5)

    def division(self):
        user_input = input("Insert the number->")
        if user_input == 0:
            print("It is impossible to divide by zero")
        else:
            for i in self.mathematics:
                print(i / int(user_input))

result = math_1()
result.mathematics.append(30)
result.mathematics.append(45)
result.mathematics.append(20)
print(result.__init__())
print(result.subtraction())
print(result.division())