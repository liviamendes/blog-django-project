from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostIndexListView.as_view(), name='index'),
    path('category/<str:category>', views.PostCategory.as_view(), name='category_post'),
    path('search/', views.PostSearch.as_view(), name='search_post'),
    path('post/<int:pk>', views.PostDetailsUpdateView.as_view(), name='post_details'),
]
