'''
def greet(Gugu):
   print(f"Hello, {Gugu}!")
   
greet("Gugu")

def add(a, b):
    return a + b

result = add(2, 5)
print(result)  # Outputs: 7
'''

def factorial(n):
  if n == 0:
    return 1
  else:
    return n*factorial(n-1)

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
    
    
greet("Bobo", "Good Mornin")
