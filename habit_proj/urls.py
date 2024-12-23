"""
URL configuration for habit_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from user import views as user_views
from habitualize import views as home_views
from manager import views as manager_views
from django.contrib.auth import views as auth_views
from manager.views import ViewBasicHabit, CreateBasicHabit, UpdateBasicHabit, DeleteBasicHabit, CreateAdvancedHabit, UpdateAdvancedHabit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_views.home, name='home'),
    path('contact/', home_views.contact, name='contact'),
    path('signUp/', user_views.signUp, name="signUp"),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='habitualize/index.html'), name="logout"),
    path('dashboard/', manager_views.dashboard, name="dashboard"),
    path('view/<int:pk>', UpdateBasicHabit.as_view(), name="view"),
    path('delete/<int:pk>', DeleteBasicHabit.as_view(), name="delete"),
    path('create/', CreateBasicHabit.as_view(), name='create'),
    path('advanced/create', CreateAdvancedHabit.as_view(), name='adv_create'),
    path('advanced/update/<int:pk>', UpdateAdvancedHabit.as_view(), name='adv_update'),
]
