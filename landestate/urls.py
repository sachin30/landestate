"""landestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from pages import views

from django.conf import settings
from django.conf.urls.static import static
admin.site.site_title="JustEstate Project"
admin.site.site_header="JustEstate Project Administration"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("pages.urls")),
    
    path("password_reset/",auth_views.PasswordResetView.as_view(template_name="pages/password_reset.html"),name="password_reset"),
    path("password_reset_done/",auth_views.PasswordResetDoneView.as_view(template_name="pages/password_reset_sent.html"),name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="pages/password_reset_form.html"),name="password_reset_confirm"),
    path("password_reset_complete/",auth_views.PasswordResetCompleteView.as_view(template_name="pages/password_reset_done.html"),name="password_reset_complete"),

    path("property_list_api/",views.PropertyList.as_view()),
    path("property_create_api/",views.PropertyCreate.as_view()),
    path("property_retrieve_api/<int:pk>/",views.PropertyRetrieve.as_view()),
    path("property_update_api/<int:pk>/",views.PropertyUpdate.as_view()),
    path("property_destroy_api/<int:pk>/",views.PropertyDestroy.as_view()),
    path("property_list_create_api/",views.PropertyListCreate.as_view()),
    path("property_retrieve_update_api/<int:pk>/",views.PropertyRetrieveUpdate.as_view()),
    path("property_retrieve_destroy_api/<int:pk>/",views.PropertyRetrieveDestroy.as_view()),
    path("property_retrieve_update_destroy_api/<int:pk>/",views.PropertyRetrieveUpdateDestroy.as_view()),



]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

