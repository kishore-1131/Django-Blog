from django.conf.urls import url
from Blog import views
from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView, PostUpdateView, PostDeleteView,UserPostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name = "home"),
    #url(r'^post/<int:pk>/$', PostDetailView.as_view(), name= "post-details"),
    path('post/<int:pk>/', PostDetailView.as_view(), name= "post-details"),
    path('post/new/', PostCreateView.as_view(), name= "post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name= "post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name= "post-delete"),
    path('post/<str:username>/', UserPostListView.as_view(), name= "user-post"),
]

