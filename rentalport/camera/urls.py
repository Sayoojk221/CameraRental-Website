
from django.urls import path
from camera import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.userregistration),
    path('login/',views.userlogin),
    path('cart/',views.user_cart),
    path('order/',views.userorder),
    path('dashboard/',views.userpage),
    path('logout/',views.logout_user),
    path('logoutphotographer/',views.logout_photographer),
    path('photographer_area/',views.photographer_base),
    path('photographer/',views.photographer_register),
    path('photographerlogin/',views.photographer_login),
    path('selectphotographer/',views.photographerselect),
    path('bookedphotographerview/',views.photographerview),
    path('userapprove/',views.UserApprovel),
    path('photoapprove/',views.Photographerapproveladmin),
    path('photobookingapprove/',views.photographerapprove),
    path('cameraadd/',views.camera_add),
    path('cameraupdate/',views.camerabooking_update),
    path('cameradelete/',views.camerabooking_delete),



]
