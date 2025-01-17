import requests
import pytest
from func import get_tallest_hero


@pytest.fixture
def mock_heroes():
    return [
        {   "id": 1,
            "name": "Hero1",
            "appearance": {"gender": "Male", "height": ["", "180 cm"]},
            "work": {"occupation": "Scientist"}
        },
        {   "id": 2,
            "name": "Hero2",
            "appearance": {"gender": "Male", "height": ["", "200 cm"]},
            "work": {"occupation": "-"}
        },
        {   "id": 3,
            "name": "Hero3",
            "appearance": {"gender": "Female", "height": ["", "175 cm"]},
            "work": {"occupation": "Teacher"}
        },
        {   "id": 4,
            "name": "Hero4",
            "appearance": {"gender": "Female", "height": ["", "160 cm"]},
            "work": {"occupation": "-"}
        },
    ]

@pytest.fixture
def mock_requests_get(monkeypatch, mock_heroes):
    def mock_get(url):
        class MockResponse:
            def __init__(self, json_data, status_code):
                self.json_data = json_data
                self.status_code = status_code

            def json(self):
                return self.json_data

        return MockResponse(mock_heroes, 200)

    monkeypatch.setattr(requests, "get", mock_get)

    # Тест на самого высокого мужчину с работой
def test_tallest_male_with_work(mock_requests_get):
    hero = get_tallest_hero("Male", True)
    assert hero["name"] == "Hero1"

    # Тест на самого высокого мужчину без работы
def test_tallest_male_without_work(mock_requests_get):
    hero = get_tallest_hero("Male", False)
    assert hero["name"] == "Hero2"

    # Тест на самую высокую женщину с работой
def test_tallest_female_with_work(mock_requests_get):
    hero = get_tallest_hero("Female", True)
    assert hero["name"] == "Hero3"

    # Тест на самую высокую женщину без работы
def test_tallest_female_without_work(mock_requests_get):
    hero = get_tallest_hero("Female", False)
    assert hero["name"] == "Hero4"

    # Тест на случай, если героев по критериям нет
def test_no_heroes_with_criteria(mock_requests_get, mock_heroes):
    mock_heroes.clear()
    hero = get_tallest_hero("Male", True)
    assert hero is None
