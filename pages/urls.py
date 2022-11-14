from django.urls import path
from . import views

#Unique namespace for pages app
app_name='pages'

urlpatterns =[
    path("", views.home , name="home"),
    path("posts/<int:pk>/<slug:slug>/", views.post_detail , name="post_detail"),


]
