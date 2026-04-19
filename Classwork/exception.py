try:
  num1=float(input("Enter first number:"))
  num2=float(input("Enter second number:"))
  print("On dividing",num1,"by",num2)
  print("Quotient:",(num1/num2))
except ValueError:
  print("Unexpected data type")
except ZeroDivisionError:
  print("Unable to divide by 0")
else:
  print("------------------------------------")
finally:
  print("Program Executed")