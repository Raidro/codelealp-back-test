from rest_framework import viewsets, status
from rest_framework.response import responses, Response
import requests
from posts import models
from posts.api import serializers
from uuid import uuid4

base_url = "https://dev.codeleap.co.uk/careers/"


class PostsViewSets(viewsets.ViewSet):
    def list_posts(self):
        response_get = requests.get(base_url)
        if response_get.status_code == 200:
            return Response({"data": response_get.text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Erro na solicitação GET . {response_get.status_code}"},
                            status=status.HTTP_404_NOT_FOUND)

    def create_posts(self):
        data = {
            "post_id": uuid4(),
            "username": "Mateus",
            "created_datetime": "2024-03-05",
            "title": "Exemplo",
            "content": "Content Exemplo"
        }

        create_response = requests.post(base_url, data)

        if create_response.status_code == 200:
            return Response({"data": create_response.text}, status=status.HTTP_200_OK)
        else:
            return Response({"error": f"Erro na solicitação POST . {create_response.status_code}"},
                            status=status.HTTP_400_BAD_REQUEST)

