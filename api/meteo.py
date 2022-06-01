import requests
# occorre installarla con il comando
# pip install requests

key = "" # incolla la API key

lat, long = 0.0, 0.0
while True:
    try:
        city = input("inserisci una città ")
        geocode = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={key}"
        risposta = requests.get(geocode)
        risultati: list = risposta.json()
        for i, el in enumerate(risultati):
            print(f'{i+1}) {el["name"]}, {el["country"]}')

        index = int(input("Scegli uno dei risultati (immetti numero) ")) - 1
        res = risultati[index]

        lat = res["lat"]
        lon = res["lon"]
    except Exception:
        print("e")
    else:
        break


weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&lang=it&units=metric"

risposta = requests.get(weather_url)
diz = risposta.json()
print("città ->", diz["name"])
print("meteo ->", diz["weather"][0])
print("vento ->", diz["wind"])
print("temperature ->", diz["main"])

air_quality_url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={key}"
risposta = requests.get(air_quality_url)
diz = risposta.json()
indice_qualità = diz["list"][0]["main"]["aqi"]
componenti = diz["list"][0]["components"]
print("Qualità aria (1-buono, 5-pessimo) -> ", indice_qualità)
print("Componenti aria -> ", componenti)


# programma che, dopo aver chiesto in input coordinate geografiche, chiami API e stampi il meteo