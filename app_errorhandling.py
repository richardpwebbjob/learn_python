# Missing colon
x = 9
if x > 5:  # SyntaxError
    print("Big number")


    # This will crash if the file doesn't exist
with open('data.txt', 'r') as f:
    content = f.read()
print("Done!")  # Never reaches here if file missing