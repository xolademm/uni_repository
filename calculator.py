
def calculator():
    print("Directions")
    while True:
        print("Enter the operation corresponding to the number that you want")
        op = int(input())

        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))
        # Addition - 1
        def addition(a, b):
            return (a + b)
        # Subtraction - 2
        def subtraction(a, b):
            return (a - b)
        # multiplication - 3
        def multiplication(a, b):
            return (a * b)
        # Division - 4
        def division(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                return (a / b)
        # Nth root - 5
        def nth_root(a, n):
            if n == 0:
                return ("division by 0 not possible")
            else:
                return (a ** (1 / n))
        # Exponents - 6
        def exponents(a, b):
            return (a ** b)
        # modulo or remainder division - 7
        def modulo(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                return (a % b)
        # integer division - 8
        def integer_division(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                return (a // b)

        if op == 1:
            print(a, " + ", b, " = ", addition(a, b))
        elif op == 2:
            print(a, " - ", b, " = ", subtraction(a, b))
        elif op == 3:
            print(a, " * ", b, " = ", multiplication(a, b))
        elif op == 4:
            x = division(a, b)
            if x.isnumeric():
                print(a, " / ", b, " = ", x)
            else:
                print(x)
        elif op == 5:
            x = nth_root(a, b)
            if x.isnumeric():
                print(a, " / ", b, " = ", x)
            else:
                print(x)
        elif op == 6:
            print(a, " ** ", b, " = ", exponents(a, b))
        elif op == 7:
            x = modulo(a, b)
            if x.isnumeric():
                print(a, " % ", b, " = ", x)
            else:
                print(x)
        elif op == 8:
            x = integer_division(a, b)
            if x.isnumeric():
                print(a, " // ", b, " = ", x)
            else:
                print(x)
        else:
            print("Invalid operation")
        s = input("Do you want to continue? y for yes, an n for no: ")
        if s == "n":
            break
        else:
            continue
