
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^daraja/stk-push$', views.stk_push_callback, name='mpesa_stk_push_callback'),

]

