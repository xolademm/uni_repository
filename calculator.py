#creating files
f1 = open("C:\\Users\\user\\Documents\\operations.txt","r+")

#allowing files to be read
c1 = f1.read()

mem = []

def calculator():
    print("Enter the operation corresponding to the number that you want")
    op = int(input())

    
    print("Directions")
    while True:
        a = float(input("Enter the first value: "))
        b = float(input("Enter the second value: "))

        # Addition - 1
        def addition(a, b):
            mem.append(f'{a} + {b} = {a+b}')
            return (a + b)
            
        
        # Subtraction - 2
        def subtraction(a, b):
            mem.append(f'{a} - {b} = {a-b}')
            return (a - b)
            

        # multiplication - 3
        def multiplication(a, b):
            mem.append(f'{a} * {b} = {a*b}')
            return (a * b)
            
        # Division - 4
        def division(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                mem.append(f'{a} / {b} = {a/b}')
                return (a / b)
        # Nth root - 5
        def nth_root(a, n):
            if n == 0:
                return ("division by 0 not possible")
            else:
                mem.append(f'{n}th root of {a} = {a **(1/n)}')
                return (a ** (1 / n))
            
        # Exponents - 6
        def exponents(a, b):
            mem.append(f'{a} to the power {b} = {a**b}')
            return (a ** b)
        
        # modulo or remainder division - 7
        def modulo(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                mem.append(f'{a} modulo {b} = {a%b}')
                return (a % b)
            

        # integer division - 8
        def integer_division(a, b):
            if b == 0:
                return ("division by 0 not possible")
            else:
                mem.append(f'{a} divided by {b} rounded down = {a//b}')
                return (a // b)

        if op == 1:
            print(a, " + ", b, " = ", addition(a, b))
        elif op == 2:
            print(a, " - ", b, " = ", subtraction(a, b))
        elif op == 3:
            print(a, " * ", b, " = ", multiplication(a, b))
        elif op == 4:
                print(a, " / ", b, " = ", division(a,b))
        elif op == 5:
            x = nth_root(a, b)
            print(a, " / ", b, " = ", x)
        elif op == 6:
            print(a, " ** ", b, " = ", exponents(a, b))
        elif op == 7:
            x = modulo(a, b)
            print(a, " % ", b, " = ", x)        
        elif op == 8:
            x = integer_division(a, b)
            print(a, " // ", b, " = ", x)           
        else:
            print("Invalid operation")

        s = input("Do you want to continue? y for yes, an n for no: ")
        if s == "n":
            break
        else:
            continue


calculator()

def SaveAll():
    with open("C:\\Users\\user\\Documents\\operations.txt", "a") as f:
            f.write("\n".join(mem) + "\n") 

SaveAll()

def DeleteAll():
    option = input("do you want to delete all data in file, enter y for yes and n for no: ")
    if option.lower() == "y":
        with open("C:\\Users\\user\\Documents\\operations.txt", "w") as f:
            f.truncate()  # This clears the file content
        print("All saved information has been deleted.")
        
    elif option.lower() == "n":
        return
    else:
        print("invalid input, data was not deleted")


DeleteAll()

