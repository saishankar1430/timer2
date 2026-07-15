class Calculator:
    def sum(self, *args):
        result = 0
        print(args)
        for num in args:
            result += num
        return result
calc = Calculator()
print(calc.sum(1,2,3,4))

