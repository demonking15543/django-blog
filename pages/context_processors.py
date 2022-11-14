from .models import Post


def my_blogs(request):
    my_blogs = Post.objects.filter(author=request.user)[:3]

    return {
        'my_blogs': my_blogs,
    }
