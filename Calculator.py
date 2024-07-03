from logo_module import logo
import os

def clear () :
  if os.name == 'nt':
        os.system('cls')

def add(n1 , n2) : 
  return n1 + n2 

def subtract(n1 , n2) :
  if n2 > n1 :
    return n2 - n1 
  else :
    return n1 - n2 
  
def multiplication(n1 , n2) :
  return n1 * n2

def divide(n1 , n2) :
  if n1 > n2 :
    return n1 / n2 
  else:
    return n2 / n1 
  
operations = {
  "+" : add , 
  "-" : subtract , 
  "*" : multiplication , 
  "/" : divide,
}

def calculator() :
  print(logo)
  number1 = float(input("Enter the first number : "))

  should_continue = True 
  while should_continue :

    for symbol in operations :
      print(symbol)
    operation_symbol = input("Pick an operation\n")
    if operation_symbol not in operations :
      print("Invalid opertation,Please try again.")
      clear()
      calculator()
      return()

      
    number2 = float(input("Enter the next number : "))

    calculation = operations[operation_symbol]
    answer = calculation(number1 , number2 )

    if input(f"Type 'y' to continue with {answer} or type 'n' to exit\n") == "y" :
      answer = number1
    else :
      should_continue = False 
      clear()
      calculator()
      
 
calculator()