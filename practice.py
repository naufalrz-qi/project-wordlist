import requests

api_key = '64698d40-d862-449e-8cfb-25dc8467c3ba'
word = "potato"
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'
res = requests.get(url)
definitions = res.json()

for definition in definitions:
    print(definition)
    print(" ")