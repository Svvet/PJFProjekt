from django.urls import path

from . import views

app_name="tickets"
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:play_id>/', views.details, name='details'),
    path('<int:performance_id>/buy', views.buy, name='buy'),
    path('register', views.register, name='register'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
]
