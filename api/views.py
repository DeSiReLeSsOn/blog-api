from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets 
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer 
from django.db.models import Q



class StandardResultsSetPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer 
    queryset = Post.objects.all()
    pagination_class = StandardResultsSetPagination



class SearchPostsView(APIView):
    def get(self, request):
        query = request.query_params.get('q')
        if query:
            posts = Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query)
            )
        else:
            posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)