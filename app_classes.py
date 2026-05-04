# app_classes.py: Dog class examples
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle

