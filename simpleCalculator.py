#This is a simple python calculator
rawAnswear = input("Enter two numbers separated by space:")
operation = input("Enter operation(*,/,+,-)")
rawAnswearSplit = rawAnswear.split()
a = rawAnswearSplit[0]
b = rawAnswearSplit[1]
a = int(a)
b = int(b)
print(a)
if operation == "*":
  c = lambda a, b: a * b
elif operation == "/":
  c = lambda a, b: a / b
elif operation == "+":
  c = lambda a, b: a + b
elif operation == "-":
  c = lambda a, b: a - b
print(c(a,b))
