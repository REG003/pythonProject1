def add(a,b):
    return(a+b)

def substraction (a,b):
    return (a-b)
def multiplication (a,b):
    return (a*b)
def division(a,b):
    return (a/b)
print("Select the type of calculation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
calculator = input("Enter choice(1/2/3/4): ")
if calculator in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if calculator == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif calculator == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif calculator == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif calculator == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print ("invalid entree")