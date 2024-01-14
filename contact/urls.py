from django.urls import path,include
from . import views

from rest_framework import routers
from blog.views import PostsViewSet,CommentsViewSet

router = routers.DefaultRouter()

router.register(r'post',PostsViewSet)
router.register(r'comment',CommentsViewSet)


urlpatterns = [
    path('api/v1/',include(router.urls)),
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('feedback/', views.CreateContact.as_view(), name="feedback"),
]
