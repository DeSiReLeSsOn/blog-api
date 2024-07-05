from django.urls import path, include
from rest_framework import routers 
from .views import PostViewSet, SearchPostsView


app_name = 'api' 


router = routers.DefaultRouter()  
router.register(r'posts', PostViewSet) 


urlpatterns = [
    path('', include(router.urls)),
    path('search/', SearchPostsView.as_view()),  
]
