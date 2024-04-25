from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,add_comment
urlpatterns = [
    # path('', views.home, name='blogapp-home'),
    path('about/', views.about, name='blogapp-about'),

    path('',PostListView.as_view(),name="blogapp-home"),
    path('post/new',PostCreateView.as_view(),name="blogapp-newpost"),
    path('post/<int:pk>/',PostDetailView.as_view(),name="blogapp-detail"),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name="blogapp-update"),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name="blogapp-delete"),
    path('post/<int:post_id>/comment/',add_comment, name='add_comment'),
]