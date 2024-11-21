from django.contrib import admin
from django.urls import path ,include
from home import views
admin.site.site_header = "VN Music Admin"
admin.site.site_title = "VN Music Portal"
admin.site.index_title = "Welcome to VN Music Portal"


urlpatterns = [
    path("", views.index, name='home'),
    # login
    path('login',views.login,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("home", views.index, name='home'),
    path("intro", views.intro, name='intro'), 
    # for profile
    path('profile/', views.profile, name='profile'),
    
    
 
]
 