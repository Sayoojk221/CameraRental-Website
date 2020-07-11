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
        number = request.POST['number']
        details = userregister(profileimage=image,username=username,email=email,password=password,city=city,state=state,pincode=pincode,number=number,status='pending')
        details.save()
        return render(request,'home.html')
    else:
        return render(request,'user/Userregister.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        login_detail = userregister.objects.all().filter(email=email,password=password)
        for item in login_detail:
            request.session['id']=item.id
        if login_detail:
            approve = userregister.objects.all().filter(email=email,status='approve')
            if approve:
                camera_data = camera.objects.all()
                return render(request,'user/dashboard.html',{'data':camera_data})
            else:
                message = 'You not approved yet!.. '
            return render(request,'user/userlogin.html',{'message':message})
        else:
            message = 'Invaild email and password '
            return render(request,'user/userlogin.html',{'message':message})
    else:
        return render(request,'user/userlogin.html')

def admin_login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['pass']
        info = admin.objects.all().filter(username=name,password=password)
        if info:
            return render(request,'admin/admin.html')
        else:
            return render(request,'admin/adminlogin.html')
    else:
        return render(request,'admin/adminlogin.html')

def UserApprovel(request):
    user_details = userregister.objects.all()
    if request.method == 'GET':
        userid = request.GET.get('id')
        userregister.objects.all().filter(id=userid).update(status='approve')
        return render(request,'admin/userapprove.html',{'user_details':user_details})
    else:
        return render(request,'admin/userapprove.html',{'user_details':user_details})


def camera_add(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        camera_details = camera(cameraimage=image,name=name,price=price,quantity=quantity)
        camera_details.save()
        return render(request,'admin/camera.html')
    else:
        return render(request,'admin/camera.html')

def camerabooking_update(request):
    if request.session.has_key('id'):
        userid = request.session['id']
        if request.method == 'POST':
            name = request.POST['name']
            number = request.POST['number']
            city = request.POST['city']
            state = request.POST['state']
            address = name+' '+city+','+state+'\n'+number
            booking.objects.all().filter(userid=userid).update(address=address)
            order = booking.objects.all().filter(userid=userid)
            return render(request,'user/order.html',{'order':order})
        else:
            user_details = userregister.objects.all().filter(id=userid)
            content = {'user_details':user_details}
            return render(request,'user/cameraupdate.html',content)
    else:
        return render(request,'user/userlogin.html')

def camerabooking_delete(request):
    userid = request.session['id']
    if request.method =='GET':
        cameraid = request.GET['id']
        booking.objects.all().filter(id=cameraid).delete()
        order = booking.objects.all().filter(userid=userid)
        return render(request,'user/order.html',{'order':order})


def userpage(request):
    if request.session.has_key('id'):
        camera_data = camera.objects.all()
        return render(request,'user/dashboard.html',{'data':camera_data})
    else:
        return render(request,'user/userlogin.html')

def logoutuser(request):
    if request.session.has_key('id'):
        del request.session['id']
        return render(request,'home.html')

def usercart(request):
    if request.session.has_key('id'):
        id1   = request.session['id']
        id2 = request.GET.get('id')
        if request.method == 'POST':
            userid = userregister.objects.get(id=id1)
            id3 = request.POST['id']
            cameraid = camera.objects.get(id=id3)
            name = request.POST['name']
            phoneno = request.POST['number']
            city = request.POST['city']
            state = request.POST['state']
            address = name+' '+city+','+state+'\n'+phoneno
            currentquantity = request.POST['currentquantity']
            number = request.POST.get('quantity')
            lastquntity = int(currentquantity) - int(number)
            camera.objects.all().filter(id=id3).update(quantity=lastquntity)
            price = request.POST['price']
            order= booking(userid=userid,cameraId=cameraid,address=address,quantity=number,price=price)
            order.save()
            camera_data = camera.objects.all()

            return render(request,'user/dashboard.html',{'data':camera_data})
        else:
            userid2=userregister.objects.all().filter(id=id1)
            cameraid2=camera.objects.all().filter(id=id2)
            return render(request,'user/cart.html',{'user':userid2,'camera':cameraid2})
    else:
        return render(request,'user/userlogin.html')


def userorder(request):
    if request.session.has_key('id'):
        id1 = request.session['id']
        order = booking.objects.all().filter(userid=id1)
        return render(request,'user/order.html',{'order':order})
    else:
        return render(request,'user/userlogin.html')

def photographer_base(request):
    return render(request,'photographer/base.html')

def photographer_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        place = request.POST['place']
        number = request.POST['contactnumber']
        details = photographer(name=name,email=email,password=password,place=place,contactnumber=number,status='pending')
        details.save()
        return render(request,'photographer/base.html')
    else:
        return render(request,'photographer/register.html')

def photographer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        login_detail = photographer.objects.all().filter(email=email,password=password)
        if login_detail:
            approve = photographer.objects.all().filter(email=email,status='approve')
            if approve:
                return render(request,'photographer/photographer.html')
            else:
                message = 'Not approved yet!'
            return render(request,'photographer/login.html',{'message':message})
        else:
            message = 'Invaild email and password '
            return render(request,'photographer/login.html',{'message':message})
    else:
        return render(request,'photographer/login.html')

def photographerselect(request):
    if request.session.has_key('id'):
        if request.method == 'POST':
            id2 = request.session['id']
            userid = userregister.objects.get(id=id2)
            id1 = request.POST['photographer']
            photoid = photographer.objects.get(id=id1)
            date = request.POST['date']
            photoname = photoid.name
            booking.objects.all().filter(userid=userid).update(cameramanname=photoname)
            details = photographerboooking(photographerid=photoid,userid=userid,date=date)
            details.save()
            camera_data = camera.objects.all()
            return render(request,'user/dashboard.html',{'data':camera_data})
        else:
            value = photographerboooking.objects.all().values('photographerid')
            current_photoid=[]
            for i in value:
                for j in i:
                    current_photoid.append(i[j])
            cameraman = photographer.objects.all()
            content = {'cameraman':cameraman,'available':current_photoid}
            return render(request,'user/photographerselect.html',content)
    else:
        return render(request,'user/dashboard.html',{'data':camera_data})

def Photographerapprovel(request):
    photo_details = photographer.objects.all()
    if request.method == 'GET':
        photoid = request.GET.get('id')
        photographer.objects.all().filter(id=photoid).update(status='approve')
        return render(request,'admin/photographerapprovel.html',{'photo_details':photo_details})
    else:
        return render(request,'admin/photographerapprovel.html',{'photo_details':photo_details})
