from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from . import serializers
from . import models
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """test api View"""

    serialzer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """returns a list of APIView features"""

        an_apiview = [
        'uses http method as function',
        'It is similer to a traditional view',
        'Gives you the most control over your logic',
        'It mapped manually to urls'
        ]

        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        """handles update on an object"""

        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """Patch reuest , only updates fields provided in the request"""

        return Response({'method':'patch'})


    def delete(self, request, pk=None):
        """Deletes an object"""

        return Response({'method':'delete'})


class HelloViewSet(viewsets.ViewSet):
    """test api viewsets"""

    serializor_class = serializers.HelloSerializer
    def list(self,request):
        """return a hello message"""

        a_viewset = [
            'Uses action create restore update partial update',
            'automatic maps to url using routers'

        ]

        return Response({'message': 'HELLO','a_viewset':a_viewset})


    def create(self, request):
        """create new hello message"""

        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUSET)


    def retrieve(self, request, pk=None):
        """Handles getting an object by its id"""

        return Response({'http method':'Get'})


    def update(self, request, pk= None):
        """Handles updating an object"""

        return Response({'http method':'update'})


    def partial_update(self, request, pk=None):
        """Handles updating a part of object"""

        return Response({'http method':'partial update'})


    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handles creating and updating profile"""

    serializer_class = serializers.UserProfileSelializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
