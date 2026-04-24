import requests

response = requests.get("https://api.github.com")
print(response.status_code)

temp = 12
if temp > 15:
    print("temp is greater than 15")
else:
    print("temp is less than 15")

 


   