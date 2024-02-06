from dataclasses import dataclass

@dataclass
class Animal:
    name: str
    age: int
    type: str

    def greet(self) -> str:
        return f"This is {self.name}. They are {self.age} years old, and is a {self.type}."

# Example usage:
if __name__ == "__main__":
    # Creating instances of the Person class using the automatically generated __init__ method
    pet1 = Animal(name="Aly", age=2, type="Hamster")
    pet2 = Animal(name="Billy", age=3, type="Gecko")

    # Accessing attributes
    print(pet1.name)
    print(pet2.age)

    # Calling a method
    greeting = pet1.greet()
    print(greeting)

