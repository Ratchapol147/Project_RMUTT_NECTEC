from django.contrib import admin
from django.urls import path, include
from api import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', include('rest_framework.urls') ,name='txtsum'),
    path('txtsum/<int:pk>', views.txtsumDetail.as_view()),
    path('txtsum/', views.txtsumDetail.as_view()),
    path('datafull/<int:pk>', views.datafullDetail.as_view()),
    

    path('service',login_required(views.api,login_url='/login'),name='api'),
    path('test/',views.ApiView.as_view()),
    path('apiindb/',views.ApiinDB.as_view()),
]