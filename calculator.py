def add(a, b):
    return a + b

def subtract(a, b):
    return a - b  

git add README.md REQUIREMENTS.md calculator.py
git commit -m "Add addition and subtraction function"
git status

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

git diff
git add calculator.py
git commit -m "Add multiply and divide functions"

def main():
    while True:
        a = float(input("First number: "))
        op = input("Operator (+ - * /): ")
        b = float(input("Second number: "))
        if op == "+":
            print("Result:", add(a, b))
        elif op == "-":
            print("Result:", subtract(a, b))
        elif op == "*":
            print("Result:", multipy(a, b))
        elif op == "/":
            print("Result:", divide(a, b))
        else:
            print("Unknown operator:", op)

if __name__ == "__main__":
    main()

