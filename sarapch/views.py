from django.shortcuts import render,redirect
from .models import Post
from .forms import UserForm
# Create your views here.
def addblog(request):
    if request.method == 'POST':    
        form = UserForm(request.POST,request.FILES)            
        if form.is_valid():           
            form.save()              
            form = UserForm()
            print(form)          
            return render(request,'blog/addblog.html',{'form':form,'msg':'successfully add'})
        else:
            return render(request,'blog/addblog.html',{'form':form,'msg':'successfully add'})
    else:
        form = UserForm()    
    return render(request, 'blog/addblog.html', {'form': form})

        

    


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})



def logout(request):    
   posts = Post.objects.all()
   return render(request, 'blog/post_list.html', {'posts': posts})
