from django.shortcuts import render
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.




def home(request):
    posts=models.Post.objects.filter(status='Publish')

    # create paginator object
    p = Paginator(posts, 5)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger :
        # if page_number is not an integer then assign the first page

        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)




    context = {
        'page_obj': page_obj,
    }

    return render(request, 'base.html', context)


def post_detail(request, pk, slug):
    post=models.Post.objects.get(
        pk=pk,
        slug=slug,
        status='Publish' )
    print(post)
    context = {
        'post': post,
    }

    return render(request, 'post_detail.html', context)
