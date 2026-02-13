import art

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2


operations = { "+" : add,
               "-" : subtract,
               "*" : multiply,
               "/" : divide

            }


def calculator():
    print(art.logo)
    n1 = float(input("What is the first number? "))
    print("List of Possible Operations:")
    print("+")
    print("-")
    print("*")
    print("/")

    calculation_sign = (input("Pick an operation: \n"))
    print(calculation_sign)
    n2= float(input("What is the next number?"))

    continuation = True

    while continuation == True:
        for key2 in operations:
            if calculation_sign == key2:
                calculation = operations[key2](n1,n2)
                n1 = calculation
                print(n1, calculation_sign,n2,"=",calculation)
        decision = input("Do you want to continue in the same or start a fresh calculator? Type 'yes or 'no'.")
        if decision == "yes":
            n2 = float(input("What is the next number? "))
            print("+")
            print("-")
            print("*")
            print("/")
            calculation_sign = (input("Pick an operation: \n"))
            continuation = True
        elif decision == "no":
            continuation = False
            print("\n"* 200)
            calculator()
        else:
            print("\n" * 200)
            print("Invalid input.Hence Programme is done")
            calculator()
            continuation = False


calculator()
