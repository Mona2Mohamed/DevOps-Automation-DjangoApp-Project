from django.urls import path
from . import views
urlpatterns = [
    
    #path('',views.index,name="addpatient"),
    path('',views.index,name="fetch"),
    path('commoninfo/fetch',views.home,name="home"),
    path('commoninfo/add',views.add,name="add"),
    
]


