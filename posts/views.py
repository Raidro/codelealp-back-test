import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class PostsLists(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get("https://dev.codeleap.co.uk/careers/")

            if response.status_code == 200:
                return Response(response.json())
            else:
                return Response({"error": response.text})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, *args, **kwargs):
        try:
            data_to_send = {'id': "1",
                            "username": "Mateus Teste",
                            "created_datetime": "null",
                            "title": "Teste",
                            "content": "OK"
                            }
            headers = {'Content-Type': 'application/json'}
            json_data = json.dumps(data_to_send)
            response = requests.post("https://dev.codeleap.co.uk/careers/", data=json_data, headers=headers)

            if response.status_code == 200:

                return Response({"success": response.json()}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": response.text}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def patch(self, request, *args, **kwargs):

        try:
            posts_id = kwargs.get('pk')
            data_to_send = {
                "title": "Mateus Teste Modificado",
                "content": "Novo conteudo"
            }
            headers = {'Content-Type': 'application/json'}
            json_data = json.dumps(data_to_send)

            url_patch = f"https://dev.codeleap.co.uk/careers/{posts_id}"

            response = requests.post(url_patch, data=json_data, headers=headers)

            if response.status_code == 200:
                return Response({"success": response.json()}, status=status.HTTP_202_ACCEPTED)

            else:
                return Response({"error": response}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
