import requests
from django.conf import settings
from django.db import IntegrityError

from characters.models import Characters


def scrape_characters() -> list[Characters]:
    url = settings.RICK_AND_MORTY_API_CHARACTERS_URL
    page_counter = 1
    characters = []

    while True:
        current_url = url + "?page=" + str(page_counter)
        res = requests.get(current_url)
        if res.status_code != 200:
            break

        for character in res.json()["results"]:
            characters.append(
                Characters(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"],
                )
            )

        page_counter += 1

    return characters


def save_characters(characters: list[Characters]) -> None:
    for character in characters:
        try:
            character.save()
        except IntegrityError:
            print("character with already saved")


def sync_characters() -> None:
    characters = scrape_characters()
    save_characters(characters)
