from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters



from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions



class HellowApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request , format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function( get, post, put, patch, delete)',
        'Is similar to a traditional Django View',
        'Gives you most control over your application logic',
        'Is mapped manually to URLs',

        ]

        return Response({'message':'Hello!!!' , 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello request with name"""
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' :message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def put(self,request, pk=None):
        """handle updating an object"""
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update of an object"""
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method':'DELETE'})



class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hellow message"""

        a_viewset = [
        'Uses actions (list,create,retrieve,update,partial_update)',
        'Automatically map to URLs using routers',
        ' provides more functionality with lesser codes',
        ]

        return Response({'message':'Hellooo' , 'a_viewset':a_viewset})

    def create(Self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data =request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name} !'
            return Response({'message' :message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )


    def retrieve(self, request, pk=None):
        """handle getting an object by its ID"""

        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """handle updating an object by its ID"""
        return Response({'http_method':'PUT'})


    def partial_update(self, request, pk=None):
        """handle partial_updating an object by its ID"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """handle removing an object by its ID"""
        return Response({'http_method':'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating, creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
