from .models import Post


def my_blogs(request):
    try:
        my_blogs = Post.objects.filter(author=request.user)
        if len(my_blogs) > 3:
            my_blogs=my_blogs[:3]
            print(my_blogs)
        return {
        'my_blogs': my_blogs,
    }
    
    except Exception:
        return {
            'my_blogs':'',

        }




