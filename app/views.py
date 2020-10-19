
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from django.shortcuts import render
from .forms import PostForm
from .forms import PostViewForm
from .models import Post

from django.contrib import messages

def post_view(request):
    queryset = Post.objects.all()
    context = {'data':queryset}
    #context["data"] = queryset
    # import pdb;pdb.set_trace()
    fom = PostViewForm()
    return render(request, "layouts/post_view.html", context)

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # messages= "Saved"
            messages.success(request, 'Your post has saved Successfully!.')
        return render(request, 'index.html', {'form': form})
    else:
            form = PostForm()
    # import pdb; pdb.set_trace()
    dat= "gulab"
    queryset = Post.objects.all()
    context = {'data':queryset, 'form':form}
    return render(request, 'layouts/post_edit.html', context)

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
