from django.urls import path
from django.contrib.auth import views as auth_views
from pages import views
app_name="pages"
urlpatterns = [
    path('',views.index,name="index"),
    path('about_us/',views.about_us,name="about_us"),
    path('user_logout',views.user_logout,name="user_logout"),
    path("property_enquiry",views.property_enquiry,name="property_enquiry"),
    path("properties/",views.property_list_display,name="property_list_display"),
    path("property_details/<slug:slug>",views.property_details,name="property_details"),
    path("contact/",views.contact, name="contact"),
    path("user_login/",views.user_login,name="user_login"),
    path("registration/",views.registration,name="registration"),
    
    path("user_logout/",views.user_logout,name="user_logout"),

    path("user_details/",views.user_details,name="user_details"),
]
