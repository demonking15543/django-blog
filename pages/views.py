from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from . import models
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import CommentForm, NeastedCommentForm, UserForm, ArticleForm
from django.contrib.auth import logout, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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



    comments = post.post_comment.all()
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
    nested_comment_form = NeastedCommentForm()
     
       
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'number_of_likes':post.number_of_likes(),
        'post_is_liked':liked,
        'nested_comment_form':nested_comment_form
    }

    return render(request, 'post_detail.html', context)

@login_required
def post_create(request):

    context = {}
    form = ArticleForm(request.POST or None)
    context['form'] = form 
    
    if request.method == 'POST':
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author=request.user

            new_post.save()
            if new_post.status=="Publish":
                messages.success(request, f"Success, Your article {new_post.title} has been published.")
            else:
                messages.success(request, f"Success, Your article {new_post.title} has been drafted.")

            return HttpResponseRedirect(reverse("pages:home")) 
    return render (request, "edit_article.html", context)            


@login_required
def post_update(request, pk, slug):
    post = get_object_or_404(models.Post, pk=pk, slug=slug, author=request.user)

    context = {}
    form = ArticleForm(request.POST or None, instance=post)
    context['form'] = form 
    
    if request.method == 'POST':
        if form.is_valid():
            new_post=form.save(commit=False)
            new_post.author=request.user    
            new_post.save()
    

            if new_post.status=="Publish":
                messages.success(request, f"Success, Your article {new_post.title} has been updated and published.")
            else:
                messages.success(request, f"Success, Your article {new_post.title} has been updated and drafted.")

            return HttpResponseRedirect(reverse("pages:home")) 
    return render (request, "edit_article.html", context)            


@login_required
def post_remove(request, pk, slug):
    post = get_object_or_404(models.Post, pk=pk, slug=slug, author=request.user)
    title=post.title
    post.delete()
    messages.success(request, f"Success, article {title} has been removed.")
    return HttpResponseRedirect(reverse("pages:home"))




    






def BlogPostLike(request, pk, slug):
    post = get_object_or_404(models.Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('pages:post_detail', args=[str(pk), str(slug)]))



def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))   



def nested_comment(request):
    post = get_object_or_404(models.Post, id=request.POST.get('post_id') )
    comment = get_object_or_404(models.Comment, id=request.POST.get('comment_id') )

    if request.method == 'POST':
        form = NeastedCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post=post
            new_comment.comment=comment
            new_comment.save()

            

    return HttpResponseRedirect(reverse("pages:post_detail", args=[str(post.pk), str(post.slug)]))




def register_request(request):
    context = {}
    form = UserForm(request.POST or None)
    context['form'] = form

    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return HttpResponseRedirect(reverse("pages:home"))

    return render (request, "registration/register.html", context)    