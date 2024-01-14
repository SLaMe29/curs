from django.views.generic import ListView, DetailView, CreateView
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Post, Comment
from .forms import CommentForm
from .serializers import PostsSerializer,CommentsSerializer
from .pagination import BasePagination
from django.db.models import Q
from rest_framework.response import Response

class PostsViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostsSerializer
    pagination_class = BasePagination
    filterset_fields = ['category']

    @action(methods=['GET'], detail=False)
    def get_admin_posts(self, request, **kwargs):
        queryset = self.get_queryset().filter(Q(author__username='admin'))
        serializer = PostsSerializer(queryset, many=True)
        data = dict()
        data['data'] = serializer.data
        return Response(data)


class CommentsViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = BasePagination

   

class HomeView(ListView):
    model = Post
    paginate_by = 9
    template_name = "blog/home.html"


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()

