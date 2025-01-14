#urls.py
from django.urls import path
from apps.users import views

app_name = 'users'

urlpatterns = [
  path('/list', views.list, name='list'),
  path('/create', views.create, name='create'),
  path('/delete/<int:pk>', views.delete, name='delete'),
  path('/update/<int:pk>', views.update, name='update'),
]