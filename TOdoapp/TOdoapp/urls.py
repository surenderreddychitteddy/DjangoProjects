"""TOdoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app import views
from django.views.generic import UpdateView,DeleteView
from app. models import todolist
urlpatterns = [
    url(r'^admin/', admin.site.urls),
        url(r'^todolist/', views.todo_list),
        url(r'^update/(?P<pk>[0-9]+)', UpdateView.as_view(model=todolist, fields="__all__",
            success_url="/todolist/")),
        url(r'^delete/(?P<pk>[0-9]+)', DeleteView.as_view(model=todolist, 
            success_url="/todolist/"),),
        # url(r'^create/', CreateView.as_view(model=todolist,
        # 	fields="__all__",
        # 	success_url="/todolist/")),
# url(r'^create/', views.Create),
url(r'^getfile/', views.getfile),



]
