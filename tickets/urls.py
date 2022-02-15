from django.urls import path

from . import views

app_name="tickets"
urlpatterns = [
    path('index', views.index, name='index'),
    path('<int:play_id>/', views.play, name='play'),
    path('register', views.register, name='register'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('performance/<int:performance_id>', views.performance, name='performance'),
    path('addTicket', views.addTicket, name='addTicket'),
    path('myTickets', views.myTickets, name='myTickets'),
]
