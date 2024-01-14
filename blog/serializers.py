from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination


from .models import Post,Category,Tag,Comment


User = get_user_model()


class PostsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),slug_field='name')
    tags = serializers.SlugRelatedField(queryset=Tag.objects.all(),many=True,slug_field='name')
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "text",
            "author",
            "category",
            "tags",
            "image",
            "create_at",
        )
    
class CommentsSerializer(serializers.ModelSerializer):
  
    post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')
    class Meta:
        model = Comment
        fields = (
            "id",
            "name",
            "email",
            "website",
            "message",
            "create_at",
            "post",
        )

        