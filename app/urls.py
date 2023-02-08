from django.urls import path, re_path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home,name='home'),
    re_path('processinpput',views.input_process,name='process_input'),
    re_path('process',login_required(views.process ,login_url='/login'),name='process'),
    
    # re_path('process',login_required(views.process ,login_url='/login'),name='process'),
   
  


]