import requests
# occorre installarla con il comando
# pip install requests

key = "" # incolla la API key

url = f"https://api.openweathermap.org/data/2.5/weather?lat=45.4654219&lon=9.1859243&appid={key}&lang=it&units=metric"

risposta = requests.get(url)
diz = risposta.json()
print("meteo ->", diz["weather"])
print("vento ->", diz["wind"])

# programma che, dopo aver chiesto in input coordinate geografiche, chiami API e stampi il meteo