"""eCommerce URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from product import  views
from product.models import Product,Cart,UserProfile
from django.views.generic import ListView,TemplateView,DetailView
# from order import  views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
        # url(r'^produts/',views.list_product),  
                url(r'^contus/',TemplateView.as_view(template_name = 'product/contus.html')),
     
         url(r'^reg/',views.SignUP),
         url(r'^login/',views.Login),
        url(r'^home/',views.home),   

                url(r'^controlpage/',views.controlpage),   
  
         # url(r'^createproduct/',views.createproduct),


         url(r'^viwecart/',views.viwecart),
                   url(r'^viwecart/',ListView.as_view(model=Cart)),

         url(r'^addcart/([0-9]+)',views.addcart),

        # url(r'^p/([0-9]+)/',views.productprofile),
    url(r'^show/(?P<pk>[0-9]+)/', DetailView.as_view(model=UserProfile)),

         url(r'^cake/',views.cake),
                  url(r'^Gift/',views.gift),
        url(r'^showcake/([0-9]+)/',views.cakeprofile),
        url(r'^showgift/([0-9]+)/',views.giftprofile),

    # url(r'^(?P<pk>[-\w]+)/', views.product_list, name='product_list_by_category'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
