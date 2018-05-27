from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """test api View"""

    def get(self, request, format=None):
        """returns a list of APIView features"""

        an_apiview = [
        'uses http method as function',
        'It is similer to a traditional view',
        'Gives you the most control over your logic',
        'It mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})
