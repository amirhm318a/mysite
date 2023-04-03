from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post,comment
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from blog.forms import commentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect


#@login_required(login_url='/accounts/login')
def blog_view(request,**kwargs):
    posts = Post.objects.filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts,3)
    
    try:
        page_number = request.GET.get('page')
        posts =posts.get_page(page_number)
        print(posts)
    except PageNotAnInteger :
        posts =posts.get_page(1)
    except EmptyPage:
        posts =posts.get_page(1)
    context= {'posts': posts}
    return render(request,'blog/blog-home.html',context)
# Create your views here.

def blog_single(request,pid):
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            form.save()
    
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)

    if not post.login_require or request.user.is_authenticated: 
        form = commentForm()
        comments = comment.objects.filter(post=post.id,approved=True) 
        context= {'post':post,'comments': comments,'form':form}
        return render(request,'blog/blog-single.html',context)
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


def test(request):
    return render(request,'test.html')

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context= {'posts': posts}
    return render(request,'blog/blog-home.html',context)



def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context= {'posts': posts}
    return render(request,'blog/blog-home.html',context)

