### CLASS ### con las clase definimos objetos con atributos o elementos que represente algo del mundo real

class Person:
  def __init__(self, name, surname, age, alias = "Sin alias"):
    self.__name = name # __ significa que es privado y no se puede modificar
    self.surname = surname # publico
    self.age = age # publico
    self.full_person = f"I am {name} {surname} and I am {age} years old. and my alias is {alias}" # publico

  
  def get_name(self):
    return self.__name

  def walk(self):
    print(f"{self.surname} is walking")
    pass


myPerson = Person("Juan", "Perez", 30, 'pechuga')
print(myPerson.full_person)
print(myPerson.get_name())
myPerson.walk()

myPerson.full_person = "I am a locombiano"
print(myPerson.full_person)
# print(myPerson.__name)


