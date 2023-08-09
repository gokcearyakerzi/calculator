def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {'+':add,
              '-': subtract,
              '*': multiply,
              '/': divide
             }
should_con = True
def calculator():
    num1 = int(input("what is the first number?"))
    for i in operations:
      print(i)
    should_con = True
    while should_con:
        operator = input("Pick an operation")
        num2 = int(input("what is the second number?"))
        calculation_function = operations[operator]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operator} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer} type 'n' to exit") == 'y':
          num1 = answer
        else:
           should_con = False
           calculator()
calculator()
