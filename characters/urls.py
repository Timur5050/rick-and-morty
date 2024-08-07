from characters.views import get_random_character

from django.urls import path, include

urlpatterns = [
    path("random/", get_random_character),
]

app_name = "characters"
