from rest_framework.response import Response
from rest_framework import status, generics, viewsets, mixins

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from cinema.models import Movie, Genre, Actor, CinemaHall
from cinema.serializers import (
    MovieSerializer,
    ActorSerializer,
    CinemaHallSerializer,
    GenreSerializer,
)


class GenreList(APIView):
    def get(self, request) -> Response:
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request) -> Response:
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    def get_object(self, pk) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ActorList(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
