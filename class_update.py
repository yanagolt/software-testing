class math_1:
    def __init__(self):
        self.mathematics = []

    def multiplication(self):
        return [i*3 for i in self.mathematics]

    def subtraction(self):
        return [i - 5 for i in self.mathematics]
    def division(self):
        user_input = input("Insert the number->")
        if user_input == 0:
            raise ZeroDivisionError
        else:
            return [i/int(user_input) for i in self.mathematics]

result = math_1()
result.mathematics.append(40.)
result.mathematics.append(45.)
result.mathematics.append(20.)
print(result.multiplication())
print(result.subtraction())
print(result.division())
