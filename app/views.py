
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django import template
from django.shortcuts import render
from .forms import PostForm
from .forms import PostViewForm
from .forms import DeleteViewForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.db.models import Count

@login_required

def post_view(request):
    queryset = Post.objects.all()
    context = {'data':queryset}
    #context["data"] = queryset
    # import pdb;pdb.set_trace()
    fom = PostViewForm()
    return render(request, "layouts/post_view.html", context)

@login_required

def delete_post_view(request,id):
    try:
        go  = Post.objects.get(id=id)
    except ObjectDoesNotExist:
        go = None
    if go == None:
        return HttpResponse('<p>  data doesnt exist </p>')
    go.delete()
    return render(request, "layouts/post_view.html", {'data': Post.objects.all()})

@login_required

def post_new(request):
    if request.method == 'POST':
        #import pdb; pdb.set_trace()
        form = PostForm(request.POST, request.FILES)
        #import pdb; pdb.set_trace()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # messages= "Saved"
            messages.success(request, 'Your post has saved Successfully!.')
        return render(request, 'index.html', {'form': form})
    else:
            form = PostForm()
    # import pdb; pdb.set_trace()
    queryset = Post.objects.all()
    #my_total = Post.objects.count()
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