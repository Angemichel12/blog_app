from django.shortcuts import render,redirect,get_object_or_404
from .models import BlogItems
from .forms import BlogForm

def home(request):
    blogs =BlogItems.objects.all()
    context={"blogs":blogs}
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def readmore(request):
    return render(request,'readmore.html')
def readmore(request,pk):
    blog=get_object_or_404(BlogItems,pk=pk)
    return render(request,'readmore.html',{'blog':blog})
def addblog(request):
    if request.method =='POST':
        form =BlogForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form=BlogForm()
    return render(request, 'addblog.html', {'form':form})