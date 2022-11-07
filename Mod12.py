# tehtävät 12.1

import requests

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url).json()
print(response['value'])


# tuntiesimerkki

'''query_param = input("Anna hakusana: ")
url = f"https://api.tvmaze.com/search/shows?q={query_param}"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if len(data) == 0:
            print("Ei hakutuloksia.")
        for item in data:
            print(f"hakutuloksen nimi: {item['show']['name']}")
            print(f"pojot: {item['score']}, "
                  f"lisätietoa: {item['show']['url']}")
    else:
        print(f"Viallinen osoite, error: {response.status_code}")
except requests.exceptions.RequestException as e:
    print("Jotain meni pieleen." + str(e))'''