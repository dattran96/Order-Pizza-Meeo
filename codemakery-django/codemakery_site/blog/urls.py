from django.urls import path

from .views import PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView
from .views import CommentCreateView
urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='post_comment'),



]



