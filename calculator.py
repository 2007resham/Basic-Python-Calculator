class calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def square(self, a):
        return a * a
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("Cannot take square root of negative number")
        return a ** 0.5
    
    def power(self, a, b):
        return a ** b

    
def main():    
    a = input("what do you want to do? (add, subtract, multiply, divide, square, square_root, power): ").strip().lower()

    if a not in ['add', 'subtract', 'multiply', 'divide', 'square', 'square_root', 'power']:
        print("Invalid operation")

    else:
        if a in ['add', 'subtract', 'multiply', 'divide', 'power']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        else:
            x = float(input("Enter number: "))

    
    calc = calculator()
    
    if a == 'add':
        print(f"Result: {calc.add(x, y)}")
    elif a == 'subtract':
        print(f"Result: {calc.subtract(x, y)}")
    elif a == 'multiply':
        print(f"Result: {calc.multiply(x, y)}")
    elif a == 'divide':
        try:
            print(f"Result: {calc.divide(x, y)}")
        except ValueError as e:
            print(e)
    elif a == 'square':
        print(f"Result: {calc.square(x)}")
    elif a == 'square_root':
        try:
            print(f"Result: {calc.square_root(x)}")
        except ValueError as e:
            print(e)
    elif a == 'power':
        print(f"Result: {calc.power(x, y)}")

if __name__=="__main__":
    main()