from django.urls import path
from . import views

#Unique namespace for pages app
app_name='pages'

urlpatterns =[
    path("", views.home , name="home"),
    path("posts/<int:pk>/<slug:slug>/", views.post_detail , name="post_detail"),
    path('blogpost-like/<int:pk>/<slug:slug>/', views.BlogPostLike, name="post_like"),
    path('nested-comment/', views.nested_comment, name="nested_comment"),
    path('logout/', views.Logout,  name='logout'),





]
