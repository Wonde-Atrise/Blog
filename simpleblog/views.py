from django.shortcuts import render,redirect
from .models import Blogmodel,Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import Blogdetails, BlogForm,UserForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
    
    blogs= Blogmodel.objects.all().order_by('id')
  
    
    return render(request,"Home.html",{'blog_value':blogs})
def Details(request, id):
    
    list = Blogmodel.objects.get(id=id)
    blog_message= list.message_set.all()
    if request.method=="POST":
        message=Message.objects.create(
            user= request.user,
            blog= list,
            body= request.POST.get('body')
        )
        return redirect('details',id= list.id)
    return render(request,'Details.html',{
        'details':list,'blog':blog_message
        
   })
    
    
def User_login( request):
   page= 'login'
  
   if request.user.is_authenticated:
        return redirect('home')

   if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    
    
   context = {'page': page}
   return render(request, 'User_login.html', context)
@login_required(login_url='login')
def CreateBlog(request):

 form = BlogForm()
    
 if request.method=="POST":

     Blogmodel.objects.create(
            User_ID=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
     return redirect('home')
    
    
    
 context={
    'form':form
   }
 return render(request, 'Createblog.html',context)     
def user_logout(request):
    
       logout(request)
       return redirect('home')
def Register(request):
      form = UserCreationForm()
  
      if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Registeration Failed')

   
      return render(request, 'Register.html', {'form': form})
@login_required(login_url='login')
def Update_blog(request,id):
    blogupdate= Blogmodel.objects.get(id=id)
    Notath="auth"
    form = Blogdetails(instance=blogupdate)
    if request.user != blogupdate.User_ID:
        Notath="NA"

    if request.method == 'POST':
        blogupdate.title = request.POST.get('title')
        blogupdate.description = request.POST.get('description')
        
        blogupdate.save()
        return redirect('home')

    context = {'form': form,'Notath':Notath }
    return render(request, 'blog_update.html', context)
@login_required(login_url='login')
def DeletBlog( request,id):
      blogdele= Blogmodel.objects.get(id=id)
   
      blogdele.delete()
      return redirect('home')  
@login_required(login_url='login') 
def User_profile(request,username):
      users = User.objects.get(username=username)
      Notath="auth"

      forms = UserForm(instance=users)
      if request.user != users.username:
        Notath="NA"
      if request.method == 'POST':
         users.username = request.POST.get('username')
         users.save()
         return redirect('home')
    
      context = {'form': forms,'Notath':Notath  }
      return render(request, 'Userprofile.html', context)
  
def delete_message(request,id):
      blog_list= Message.objects.get(id=id)
      
      blog_list.delete()
      return redirect('home')
      
