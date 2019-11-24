from django.urls import path, reverse_lazy
from django.views.generic import TemplateView
from . import views
from django.conf.urls import url


app_name='home'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home/hello.html'), name='home'),
    #path('profile/', views.UserFormView.as_view(), name='register'),
    url(r'^signup/$', views.signup, name='signup'),

]