import requests


def get_tallest_hero(gender, has_work):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Не удалось получить данные с API")

    heroes = response.json()

    # фильтрация по входным данным
    if has_work:
        filtered_heroes = [hero for hero in heroes if hero.get("appearance", {}).get("gender") == gender
                           and hero.get("work", {}).get("occupation") != '-']
    else:
        filtered_heroes = [hero for hero in heroes if hero.get("appearance", {}).get("gender") == gender
                           and hero.get("work", {}).get("occupation") == '-']
    if not filtered_heroes:
        return None

    tallest_hero = max(filtered_heroes, key=lambda h: float(h.get("appearance", {}).get("height", ["0"])[1].split()[0]))
    return tallest_hero
