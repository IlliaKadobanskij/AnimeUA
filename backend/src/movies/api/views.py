from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.generics import ListAPIView

from .serializers import MovieSerializer, ShadowMovieSerializer
from movies.models import Movie, ShadowMovie
from rest_framework.response import Response
from rest_framework.views import APIView

from ..bucket import create_presigned_url1


@permission_classes((permissions.AllowAny,))
class MovieDetailView(APIView):
    def get(self, request, pk):
        movie = Movie.objects.get(id=pk)

        link_array = [create_presigned_url1(str(video.bucket_id), str(video.name)) for video in
                      movie.video.all()]

        shadow = ShadowMovie(id=1, title=movie.title, description=movie.description, poster=movie.poster,
                             year=movie.year, country=movie.country, category=movie.category,
                             url=movie.url, rating=movie.rating, video_urls=link_array)

        for genre in movie.genres.all():
            shadow.save()
            shadow.genres.add(genre)

        serializer = ShadowMovieSerializer(shadow)
        return Response({"movie_data": serializer.data})


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer