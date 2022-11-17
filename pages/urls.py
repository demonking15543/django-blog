from django.urls import path
from . import views

#Unique namespace for pages app
app_name='pages'

urlpatterns =[
    path("", views.home , name="home"),
    path("posts/<int:pk>/<slug:slug>/", views.post_detail , name="post_detail"),
    path("posts/create/", views.post_create , name="post_create"),
    path("posts/update/<int:pk>/<slug:slug>/", views.post_update , name="post_update"),
    path("posts/remove/<int:pk>/<slug:slug>/", views.post_remove , name="post_remove"),

    path('blogpost-like/<int:pk>/<slug:slug>/', views.BlogPostLike, name="post_like"),
    path('nested-comment/', views.nested_comment, name="nested_comment"),
    path('logout/', views.Logout,  name='logout'),
    path("accounts/register", views.register_request, name="register")






]
