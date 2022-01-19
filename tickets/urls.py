from django.urls import path

from . import views

app_name="tickets"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:play_id>/', views.details, name='details'),
    path('<int:performance_id>/buy', views.buy, name='buy'),
]
