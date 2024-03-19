from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import Category,Product,Coustmer

#for api
from rest_framework import generics
from .models import APIKey
from .serializers import APIKeySerializer
from .authentication import APIKeyAuthentication

def index(request):
    return render(request, 'index.html')
@login_required(login_url='login')


def collections(request):
    category= Category.objects.filter(status=0)
    
    return render(request,'collections.html',{"category":category})

def loginn(request):
     if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']
         user=auth.authenticate(username=username,password=password)
         if user is not None:
            auth.login(request,user)
            return redirect("/")
         else:
            messages.info(request,'invalid login')
            return redirect('login')
        
    
     return render(request,'layout/login.html')

def register(request):
    if request.method=="POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirm-password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exists")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"this email already exists") 
            return redirect("register")
        elif password !=confirmpassword:
            messages.info(request,"password no match ")
            return redirect("register")
            
        else: 
          user=User.objects.create_user(username=username,email=email,password=password)
          user.save()
          return redirect('/')
        
    else:
            
        return render(request,'layout/register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug,status=0)):
       product= Product.objects.filter(category__slug=slug)
    else:
        messages.error(request,"no")
        return redirect("collections")
    return render(request,'layout/product.html',{"product":product})



def productview(request,cate_slug,prod_slug):
    if(Category.objects.filter(slug=cate_slug,status=0)):
            if(Product.objects.filter(slug=prod_slug,status=0)):
                aswanth=Product.objects.filter(slug=prod_slug,status=0)
            else:
               messages.error(request,'no such product found')
               return redirect('collections')                
    
    
    else:
        messages.error(request,"no such category found")
        return redirect("collections")
    return render(request,"layout/productview.html",{"aswanth":aswanth})    



def coustmerdet(request):
    n=''
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        en=Coustmer(name=name,email=email,phone=phone,address=address)
        en.save()
        n='data inserted'
      
    return render(request,'contact.html')

def payment(request):
    return render(request,'payment.html')



#for api
# views


class APIKeyListCreateView(generics.ListCreateAPIView):
    authentication_classes = (APIKeyAuthentication,)
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer

class APIKeyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (APIKeyAuthentication,)
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer
