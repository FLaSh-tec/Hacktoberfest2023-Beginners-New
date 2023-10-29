def calculate(num1, num2, operator):
  """Performs a calculation on two numbers."""

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    return num1 / num2
  else:
    raise ValueError("Invalid operator")

def main():
  

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Enter the operator (+, -, *, or /): ")

  result = calculate(num1, num2, operator)

  print("The result is:", result)

if __name__ == "__main__":
  main()
