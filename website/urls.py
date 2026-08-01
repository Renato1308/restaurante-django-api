from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ou a função que renderiza sua página inicial
]