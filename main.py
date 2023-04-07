import requests

URL = 'https://akabab.github.io/superhero-api/api/all.json'
data = requests.get(URL)
hero_list = data.json()

need_heroes = ['Hulk', 'Captain America', 'Thanos']
intelligence_heroes = {}

for hero in hero_list:
    for need_hero in need_heroes:
        if need_hero in hero['biography']['fullName'] or need_hero in hero['biography']['aliases']:
            intelligence_heroes[need_hero] = hero['powerstats']['intelligence']

sorted_hero = sorted(intelligence_heroes, key=intelligence_heroes.get, reverse=True)

if __name__ == '__main__':
    print(f'Самый сильный супергерой это: {sorted_hero[0]}, '
          f'который имеет силу {intelligence_heroes["Thanos"]}')