import requests

    


longitude = 2.35
latitude =48.85

latitude = 33.45
longitude= -112.073891

# temperature = 50

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

print(url)

response = requests.get(url)
data = response.json()
temperature = data["current"]["temperature_2m"]
print(f"Temperature in Phoenix is {temperature * 9/5 + 32} ")




