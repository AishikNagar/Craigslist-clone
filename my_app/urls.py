from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/',admin.site.urls),
    path('new_search',views.new_search,name='new_search')
]