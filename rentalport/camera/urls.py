
from django.urls import path
from camera import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.userregistration),
    path('login/',views.userlogin),
    path('cart/',views.usercart),
    path('order/',views.userorder),
    path('dashboard/',views.userpage),
    path('logout/',views.logoutuser),
    path('photographer_area/',views.photographer_base),
    path('photographer/',views.photographer_register),
    path('photographerlogin/',views.photographer_login),
    path('selectphotographer/',views.photographerselect),
    path('userapprove/',views.UserApprovel),
    path('photoapprove/',views.Photographerapprovel),
    path('cameraadd/',views.camera_add),
    path('cameraupdate/',views.camerabooking_update),
    path('cameradelete/',views.camerabooking_delete),

]
