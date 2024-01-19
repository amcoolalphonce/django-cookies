from django.contrib import admin
from django.urls import path
from store import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('index/', views.index),
  path('scookie/', views.setcookie),
  path('gcookie/', views.getcooki)
]
# assuming that you have a  python django app already
