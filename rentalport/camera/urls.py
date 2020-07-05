
from django.urls import path
from camera import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.userregistration),
    path('login/',views.userlogin),



]
