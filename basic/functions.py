def hello(name="world"):
  return print(f"hello {name}")

hello("Alice")
hello("Bob")
hello()



sum = lambda x, y: print(x + y)

sum(5,6)

def hello(*name):
    for n in name:
        print(f"Hello, {n}!")

hello("Alice", "Bob", "Charlie")