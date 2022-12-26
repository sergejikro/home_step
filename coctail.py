import requests

def response():
    r = requests.get('https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a')
    data = r.json()
    arr = ''
    for item in data['drinks']:
        arr += (f"Cocktail:{item['strDrink']}; How to prepare: {item['strInstructions']}; Link to photo: {item['strDrinkThumb']}\n")
        return arr

def record(x):
    with open('cocktail.txt', 'w+') as f:
        f.write(x)



record(response())

