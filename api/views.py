from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import authentication,permissions
from rest_framework.decorators import action


from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.response import Response
from api.serializers import UserSerializer,MovieSerializer,ReviewSerializer
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,CreateModelMixin
from myapp.models import Movies,Reviews,Genres

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user==obj.user
    

class UsersView(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()
    model=User
    http_method_names=["post"]

class MoviesView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = MovieSerializer
    model = Movies
    queryset = Movies.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    # localhost:8000/api/movies/{id}/add_review/
    # data:{comment,rating}
    @action(methods=["post"], detail=True)
    def add_review(self, request, *args, **kwargs):
        movie_obj = Movies.objects.get(pk=kwargs.get('pk'))
        user = request.user
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(movie=movie_obj, user=user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors)
    
    @action(methods=["get"],detail=False)
    def genres(self,request,*args,**kwargs):
        qs=Genres.objects.all().values_list("genre",flat=True).distinct()
        return Response(data=qs)

    # localhost:8000/api/movies/?genre=comedy
    def list(self,request,*args,**kwargs):
        qs=Movies.objects.all()
        if "genre" in request.query_params:
            genre_name=request.query_params.get("genre")
            genre_obj=Genres.objects.get(genre=genre_name)
            qs=genre_obj.movies_set.all()
        serializer=MovieSerializer(qs,many=True)
        return Response(data=serializer.data)

# edit delete
class Reviewsview(GenericViewSet,DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin):
    serializer_class=ReviewSerializer
    queryset=Reviews.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsOwner]