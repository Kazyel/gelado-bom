from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('picoles', views.picoles, name='picoles'),
    path('sorvetes', views.sorvetes, name='sorvetes & acai'),
    path('updatepicoles', views.update_picole, name="update picoles"),
    path('updatesorvetes', views.update_sorvetes, name="update sorvetes"),
]