a = input("Enter a number: ")
assert a.isdigit(), "You must enter a number!" 
print(f"Entered number: {a}")

class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Length must be greater than 0!"
        assert type in ["square", "rectangle", "triangle"], "Allowed figures: square, rectangle, triangle"
        self.type = type
        self.length = length

c = Figure("square", 5)
print(f"Figure: {c.type}, Length: {c.length}")

class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Andriy", "Anonymous", "Maxim"]: 
            raise ValueError("Allowed names: Andriy, Anonymous, Maxim")
        if not hobby: 
            raise ValueError("Hobby field cannot be empty")
        self.name = name
        self.hobby = hobby

a = Name("Maxim", "Programming")
print(f"Name: {a.name}, Hobby: {a.hobby}")
