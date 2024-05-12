foods = [ "apple", "banana", "cherry", "meat", "elderberry", "sugar", "coke" ]
number = 3

#For loop
for food in foods:
    if food == "meat":
        print("I don't eat meat")
        continue
    elif food == "sugar" or food == "coke":
        print("I don't eat sugar nor drink coke")
        break
    print("I like", food)

print("End of the loop")
print("")

#While loop

while number < 10:
    print(number)
    number += 1