from django.shortcuts import render
from camera.models import *
def home(request):
    return render(request,'home.html')

def userregistration(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['zip']
        details = userregister(profileimage=image,username=username,email=email,password=password,city=city,state=state,pincode=pincode)
        details.save()
        return render(request,'home.html')
    else:
        return render(request,'Userregister.html')

def userlogin(request):
    return render(request,'userlogin.html')

def admin(request):
    return render(request,'admin.html')
