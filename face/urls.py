from django.urls import path
from . import views 
urlpatterns = [
    #path('',views.test1, name='test1'),
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('coffee',views.coffee,name='coffee')
]
