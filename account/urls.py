from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('loginotp/', views.OtpLoginView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('check/', views.CheckOtpView.as_view(), name='check'),
]
