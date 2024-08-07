import random

from characters.models import Characters

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from characters.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    pks = Characters.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Characters.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data)
