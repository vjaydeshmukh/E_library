from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('logout/', views.user_logout, name="logout"),
    path('logout/', views.user_logout, name="login"),
    path('logout/', views.user_logout, name="signup"),
]
