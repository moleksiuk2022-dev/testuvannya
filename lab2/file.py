import sys
import keyword
from random import randint
a = "text variable" 
b = 1            
b1 = 1.1          
c = ["a", 1, 1.25, "Word", a]
d = {
    "a": "Word",
    "b": 1,
    a: b
}
e = ("a", a)
f = {"ss", a + str(b)}
print("Variable a:", a)
print("Variable b:", b)
print("Variable b1:", b1)
print("List c:", c)
print("Dictionary d:", d)
print("Tuple e:", e)
print("Set f:", f)
print("First constant:", True)
print("Second constant:", False)
print(f"Formatted output example: {None}")


print("\nPython reserved keywords:")
print(keyword.kwlist)
text = "Hello, Python!"
print("\nlen():")
print(f"length row '{text}' =", len(text))
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"This is a {fruit}")
print("\n" + "-"*20)
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
B = randint(0, 5)
print(f"B is even: {B}" if B % 2 == 0 else f"B is odd: {B}")
A = 0

try:
    print("What happens if we divide 10 by", A, "?")
    result = 10 / A  
except Exception as e:
    print("Oops! There was an error:", e)
finally:
    print("Finally block always executes!")
with open("example.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
with open("example.txt", "r") as f:
    for index, line in enumerate(f):
        print(f"{index})> {line.strip()}")

greet = lambda name: f"Hello, {name}!"
print(greet("Maksim"))
add = lambda x, y: x + y
print("3 + 5 =", add(3, 5))
print("10 + 20 =", add(10, 20))
