from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm

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
    post=get_object_or_404(
        models.Post,
        pk=pk,
        slug=slug,
        status='Publish' )



    comments = post.post_comment.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    liked = False
    if post.likes.filter(id=request.user.id).exists():
        liked = True
    

    
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'number_of_likes':post.number_of_likes(),
        'post_is_liked':liked
    }

    return render(request, 'post_detail.html', context)



def BlogPostLike(request, pk, slug):
    post = get_object_or_404(models.Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('pages:post_detail', args=[str(pk), str(slug)]))



def login(request):
    return render(request, 'login.html')    