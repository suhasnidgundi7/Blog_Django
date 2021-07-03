from django.urls import path
from . import views
from .views import HomeView, PostDetailView, AddPostView, UpdatePostView, DeletePostView, OlderPostView, AddCategoryView, LikeView, AddCommentView

urlpatterns = [

    path('', HomeView.as_view(), name='home'),
    path('older_post/', OlderPostView.as_view(), name='older_post'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),

    path('category/<str:cats>/', views.CategoryView, name='category'),
    path('like/<int:pk>/', LikeView, name='like_post'),

    
]
