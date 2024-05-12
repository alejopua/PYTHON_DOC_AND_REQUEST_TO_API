numberOne, numberTwo, numberTree = 1, 2, "3"

try:
  print(numberOne + numberTwo)
  print("Process is good")
except ValueError: 
  print("Process is bad, value error")
except TypeError: 
  print("Process is bad, type error")
except Exception: 
  print("Process is bad, exception error")
else: # optional
  print("Process is continuing correctly")
finally: # optional
  print("Process is continue")


print(numberOne + numberTree)

