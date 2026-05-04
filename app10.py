# app10.py: list creation and manipulation
age = 25
has_license = False
my_list = ["Alice", 25, age, True, has_license]

nane = my_list[0]
age = my_list[1]

has_license = my_list[-3]

my_list[0] = "Richard"

my_list.append("Alice")

print(my_list)

my_list.remove("Alice")

my_list.insert(1, "Alice")

print(my_list)
