from rest_framework import viewsets

from django.utils.encoding import force_text
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

import json
from .models import MoviesSuggestor

class Hello(APIView):
    def get(self, request):
        return Response({"hello": "world"})
    

# your ml class here
class MoviesSuggestionView(APIView):
    def get(self, request):
        name = request.GET.get('name', 'Star Wars (1977)')
        movies_list = MoviesSuggestor().suggest(name)
        return Response({
            "suggested_movies":movies_list
            })
    