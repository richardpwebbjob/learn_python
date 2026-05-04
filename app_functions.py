# app_functions.py: utility functions and examples
def greet(first_name, last_name="Jones"):
    print(f"Hello! {first_name} {last_name}")

greet(first_name="Richard", last_name="Webb")
greet(first_name="James")

# Print a message depending on the temperature threshold
def check_weather(temperature):
    # temperature = 96
    if temperature > 25:
        print("It's hot!")
    else:
        print("The weather is nice!")

check_weather(temperature=90)

# Calculate the total price after tax and discount
def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    total_price = price + tax - (price * discount)
    message = (f"Total Price: ${total_price}")
    return message

result = calculate_total(100, .08, .20)
print(result)

# Compute area and add a small overhead factor
def calculate_area(width, height):
    area = width * height
    area = area * 1.05
    return area

result = calculate_area(width=10, height=12)
print(f"Room size is {result} sq feet")

# Double the provided number
def double(number):
    return number * 2

result = double(10)
print(result)

print(double(50))

# Return the first and last number from a list
def simple_function():
    numbers = [1,2,3,4,5]
    first_number = numbers[0]
    second_number = numbers[1]
    last_number = numbers[-1]
    return first_number, last_number

first, last = simple_function()
print(first)
print(last)

print(simple_function())




