"""
URL configuration for coursework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from mif import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.main, name="main"),

    path("signupuser/", views.signupuser, name="signupuser"),
    path("loginuser/", views.loginuser, name="loginuser"),
    path("currentuser/", views.currentuser, name="currentuser"),
    path("logoutuser/", views.logoutuser, name="logoutuser"),

    path("login_employee/", views.login_employee, name="login_employee"),
    path("accountant/", views.accountant, name="accountant"),
    path("manager/", views.manager, name="manager"),
    path("analyst/", views.analyst, name="analyst"),
    path("director/", views.director, name="director"),

    path("director/view_pdf/<int:report_id>/", views.view_pdf, name='view_pdf'),
]
