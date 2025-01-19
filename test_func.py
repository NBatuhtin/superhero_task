from func import get_tallest_hero
import requests
import pytest


    # Тест на самого высокого мужчину с работой
def test_tallest_male_with_work():
    hero = get_tallest_hero("Male", True)
    assert hero is not None, "Ожидался герой, но получено None"
    assert hero.get("appearance", {}).get("gender", "") == "Male", "Неверный пол героя"
    assert hero.get("work", {}).get("occupation", "") != "-", "Герой должен иметь работу"

    # Тест на самого высокого мужчину без работы
def test_tallest_male_without_work():
    hero = get_tallest_hero("Male", False)
    assert hero is not None, "Ожидался герой, но получено None"
    assert hero.get("appearance", {}).get("gender", "") == "Male", "Неверный пол героя"
    assert hero.get("work", {}).get("occupation", "") == "-", "Герой не должен иметь работу"

    # Тест на самую высокую женщину с работой
def test_tallest_female_with_work():
    hero = get_tallest_hero("Female", True)
    assert hero is not None, "Ожидался герой, но получено None"
    assert hero.get("appearance", {}).get("gender", "") == "Female", "Неверный пол героя"
    assert hero.get("work", {}).get("occupation", "") != "-", "Герой должен иметь работу"

    # Тест на самую высокую женщину без работы
def test_tallest_female_without_work():
    hero = get_tallest_hero("Female", False)
    assert hero is not None, "Ожидался герой, но получено None"
    assert hero.get("appearance", {}).get("gender", "") == "Female", "Неверный пол героя"
    assert hero.get("work", {}).get("occupation", "") == "-", "Герой не должен иметь работу"

    # Тест на случай, если героев по критериям нет
def test_no_heroes_with_criteria():
    hero = get_tallest_hero("Unknown", True)
    assert hero is None, "Ожидалось None, но получен герой"

    # Тест на доступность API
def test_api_response_status():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    assert response.status_code == 200, f"API недоступно, код ответа: {response.status_code}"

    # Проверка на неверный тип данных для gender
def test_invalid_gender_type():
    with pytest.raises(TypeError):
        get_tallest_hero(12345, True)

    # Проверка на неверный тип данных для has_work
def test_invalid_has_work_type():
    with pytest.raises(TypeError):
        get_tallest_hero("Male", "Yes")
