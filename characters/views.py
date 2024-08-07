import random

from rest_framework.generics import ListAPIView

from characters.models import Characters

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from characters.serializers import CharacterSerializer


@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    pks = Characters.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Characters.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=HTTP_200_OK)


class ListCharacters(ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        queryset = Characters.objects.all()

        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
