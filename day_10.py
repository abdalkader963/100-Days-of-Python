#calculater first try myself
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
goal=False
def Multiplication(number1,number2):
    final=number1*number2
    return final
def Subtraction(number1,number2):
    final=number1-number2
    return final
def Addition(number1,number2):
    final=number1+number2
    return final
def Division(number1,number2):
    final=number1/number2
    return final
while not goal:
    num1=float(input("What's the first number?:  "))
    operation=input("+\n-\n*\n/\nPick an operation: ")
    num2=float(input("What's the next number?:  "))
    if operation=="+":
        answer=Addition(num1,num2)
    elif operation=="-":
        answer=Subtraction(num1,num2)
    elif operation=="*":
        answer=Multiplication(num1,num2)
    elif operation=="/":
        answer=Division(num1,num2)
    print(f"YOUR FINAL ANSWER IS {answer}")
    new=input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation: ")       
    if new=="y":
        num1=answer
        goal=False
        goal2 =False
        while not goal2:
            operation=input("+\n-\n*\n/\nPick an operation: ")
            num2=float(input("What's the next number?:  "))
            if operation=="+":
                answer=Addition(num1,num2)
            elif operation=="-":
                answer=Subtraction(num1,num2)
            elif operation=="*":
                answer=Multiplication(num1,num2)
            elif operation=="/":
                answer=Division(num1,num2)
            new=input(f"Type 'y' to continue calculating with {answer} , or type 'n' to start a new calculation: ")  
            if  new=="y":
                num1=answer
                goal=False
            else:
                goal=True
                clear_screen()
    elif new=="n":
        clear_screen()
        goal=False
        goal2=True
#second try (after i made some research and used the help of AI)
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Multiplication(number1, number2):
    return number1 * number2

def Subtraction(number1, number2):
    return number1 - number2

def Addition(number1, number2):
    return number1 + number2

def Division(number1, number2):
    if number2 == 0:
        return "Error: Division by zero"
    return number1 / number2

def calculator():
    clear_screen()
    goal = False
    num1 = float(input("What's the first number?: "))

    while not goal:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        num2 = float(input("What's the next number?: "))

        if operation == "+":
            answer = Addition(num1, num2)
        elif operation == "-":
            answer = Subtraction(num1, num2)
        elif operation == "*":
            answer = Multiplication(num1, num2)
        elif operation == "/":
            answer = Division(num1, num2)
        else:
            answer = "Invalid Operation"

        print(f"YOUR FINAL ANSWER IS {answer}")

        if isinstance(answer, str): 
            new = input("Type 'n' to start a new calculation or 'e' to exit: ")
        else:
            new = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if new == "y" and not isinstance(answer, str):
            num1 = answer
        elif new == "n":
            goal = True
            calculator() 
        else:
            goal = True
            print("Goodbye!")

# if __name__ == "__main__":
#     calculator()