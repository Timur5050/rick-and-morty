from characters.views import get_random_character, ListCharacters

from django.urls import path

urlpatterns = [
    path("random/", get_random_character),
    path("characters/", ListCharacters.as_view())
]

app_name = "characters"
