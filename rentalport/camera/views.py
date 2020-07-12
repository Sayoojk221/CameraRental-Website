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
        details = userregister(profileimage=image,username=username,email=email,password=password,city=city,state=state,pincode=pincode,number=number,status='pending',camera='off')
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
            approve_check= userregister.objects.all().filter(email=email,status='approve')
            if approve_check:
                fullcamera_details = camera.objects.all()
                return render(request,'user/dashboard.html',{'data':fullcamera_details})
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
        admin_info = admin.objects.all().filter(username=name,password=password)
        if admin_info:
            return render(request,'admin/admin.html')
        else:
            return render(request,'admin/adminlogin.html')
    else:
        return render(request,'admin/adminlogin.html')

def UserApprovel(request):
    user_details = userregister.objects.all()
    userid = request.GET.get('id')
    userregister.objects.all().filter(id=userid).update(status='approve')
    return render(request,'admin/userapprove.html',{'user_details':user_details})


def camera_add(request):
    if request.method == 'POST':
        image = request.FILES['image']
        name = request.POST['name']
        price = request.POST['price']
        quantity = request.POST['quantity']
        adding_details = camera(cameraimage=image,name=name,price=price,quantity=quantity)
        adding_details.save()
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
            booked_camera_details = booking.objects.all().filter(userid=userid)
            return render(request,'user/order.html',{'order':booked_camera_details})
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
        booked_camera_details = booking.objects.all().filter(userid=userid)
        return render(request,'user/order.html',{'order':booked_camera_details})


def userpage(request):
    if request.session.has_key('id'):
        fullcamera_details = camera.objects.all()
        return render(request,'user/dashboard.html',{'data':fullcamera_details})
    else:
        return render(request,'user/userlogin.html')

def logout_user(request):
    if request.session.has_key('id'):
        del request.session['id']
        return render(request,'home.html')
    else:
        return render(request,'user/userlogin.html')
def logout_photographer(request):
    if request.session.has_key('photoid'):
        del request.session['photoid']
        return render(request,'photographer/base.html')
    else:
        return render(request,'photographer/login.html')

def user_cart(request):
    if request.session.has_key('id'):
        user = request.session['id']
        if request.method == 'POST':
            cameraid = request.POST['id']
            user_id = userregister.objects.get(id=user)
            camera_id = camera.objects.get(id=cameraid)
            user_name = request.POST['name']
            phoneno = request.POST['number']
            city = request.POST['city']
            state = request.POST['state']
            address = user_name+' '+city+','+state+'\n'+phoneno
            current_quantity = request.POST['currentquantity']
            quantity = request.POST.get('quantity')
            last_quntity = int(current_quantity) - int(quantity)
            camera.objects.all().filter(id=cameraid).update(quantity=last_quntity)
            price = request.POST['price']
            order= booking(userid=user_id,cameraId=camera_id,address=address,quantity=quantity,price=price)
            order.save()
            fullcamera_details = camera.objects.all()
            return render(request,'user/dashboard.html',{'data':fullcamera_details})
        else:
            cameraid = request.GET.get('cart_id')
            user_id=userregister.objects.all().filter(id=user)
            camera_id=camera.objects.all().filter(id=cameraid)
            return render(request,'user/cart.html',{'user':user_id,'camera':camera_id})
    else:
        return render(request,'user/userlogin.html')


def userorder(request):
    if request.session.has_key('id'):
        id1 = request.session['id']
        booked_camera_details = booking.objects.all().filter(userid=id1)
        return render(request,'user/order.html',{'order':booked_camera_details})
    else:
        return render(request,'user/userlogin.html')

def photographer_base(request):
    if request.session.has_key('photoid'):
        return render(request,'photographer/photographer.html')
    else:
        return render(request,'photographer/login.html')

def photographer_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        place = request.POST['place']
        number = request.POST['contactnumber']
        photographer_details = photographer(name=name,email=email,password=password,place=place,contactnumber=number,status='pending')
        photographer_details.save()
        return render(request,'photographer/base.html')
    else:
        return render(request,'photographer/register.html')

def photographer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        login_detail = photographer.objects.all().filter(email=email,password=password)
        if login_detail:
            approve_check = photographer.objects.all().filter(email=email,status='approve')
            for i in approve_check:
                request.session['photoid'] = i.id
            if approve_check:
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
            user = request.session['id']
            user_id = userregister.objects.get(id=user)
            photoid = request.POST['photographer']
            photographer_id = photographer.objects.get(id=photoid)
            date = request.POST['date']
            photographer_booking = photographerboooking(photographerid=photographer_id,userid=user_id,date=date,status='pending')
            photographer_booking.save()
            fullcamera_details = camera.objects.all()
            return render(request,'user/dashboard.html',{'data':fullcamera_details})
        else:
            value = photographerboooking.objects.all().values('photographerid')
            total_photographer_id=[]
            for i in value:
                for j in i:
                    total_photographer_id.append(i[j])
            photographer_details = photographer.objects.all()
            content = {'cameraman':photographer_details,'available':total_photographer_id}
            return render(request,'user/photographerselect.html',content)
    else:
        return render(request,'user/dashboard.html',{'data':camera_data})

def Photographerapproveladmin(request):
    photographer_details = photographer.objects.all()
    if request.method == 'GET':
        photographer_id = request.GET.get('id')
        photographer.objects.all().filter(id=photographer_id).update(status='approve')
        return render(request,'admin/photographerapprovel.html',{'photo_details':photographer_details})


def photographerview(request):
    if request.session.has_key('id'):
        user = request.session['id']
        photographer_id=photographerboooking.objects.all().filter(userid=user).values('photographerid')
        booked_photographer_id=0
        for i in photographer_id:
            for j in i:
                booked_photographer_id = i[j]
        photographer_details = photographer.objects.all().filter(id=booked_photographer_id)
        status = photographerboooking.objects.all().filter(userid=user,status='approved')
        content = {'order':photographer_details,'status':status}
        return render(request,'user/photographerbooked.html',content)

def photographerapprove(request):
    if request.session.has_key('photoid'):
        photographer_id = request.session['photoid']
        if request.method == 'GET':
            id1 = request.GET.get('id')
            photographerboooking.objects.all().filter(id=id1).update(status='approved')
            user_deatils = photographerboooking.objects.all().filter(photographerid=photographer_id).values('userid')
            photoid_deatils = photographerboooking.objects.all().filter(photographerid=photographer_id)
            user_id=0
            for i in user_deatils:
                for j in i:
                    user_id = i[j]
            user_view = userregister.objects.all().filter(id=user_id)
            return render(request,'photographer/approve.html',{'deatils':user_view,'photoid':photoid_deatils})
    else:
        return render(request,'photographer/login.html')

