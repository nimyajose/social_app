from django.urls import path
from . import views

app_name = "app-login"

urlpatterns = [
        path('signup/', views.sign_up, name='signup'),
        path('login/', views.login_page,name='login')

]