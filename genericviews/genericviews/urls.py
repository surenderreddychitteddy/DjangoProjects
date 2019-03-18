"""genericviews URL Configuration

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
from app.models import college,student
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
        url(r'^hello/', views.hello),

        url(r'^index/', TemplateView.as_view(template_name="index.html")),
                url(r'^create/', CreateView.as_view(
                	model=college,
                	    	fields="__all__",    	success_url="/create/",

)),
        url(r'^studentcreate/', CreateView.as_view(model=student,
        	fields="__all__",
        	success_url="/studentcreate/",)),

        url(r'^display/', ListView.as_view(model=student,)),

        url(r'^list/', ListView.as_view(model=college,)),
        url(r'^updatestudent/(?P<pk>[0-9]+)', UpdateView.as_view(model=student, fields="__all__",
            success_url="/display/")),
        url(r'^deletestudent/(?P<pk>[0-9]+)', DeleteView.as_view(model=student, 
            success_url="/display/"),),


]
