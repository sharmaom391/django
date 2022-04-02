from django.shortcuts import render,redirect
from .models import Short_URL
from .forms import UrlForm
from .shortner import Shortner

# Create your views here.
def home(request,token):
    long_url=Short_URL.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)
def index(request):
    form=UrlForm(request.POST)
    short_url=''
    if request.method=="POST":
        if form.is_valid():
            NewUrl=form.save(commit=False)
            short_url=Shortner().issue_token()
            NewUrl.short_url=short_url
            NewUrl.save()
        else:
            form=UrlForm()
            short_url="Invalid URL"

    return render(request,'index.html',{'form':form,'short_url':short_url})