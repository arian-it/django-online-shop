from django.urls import path
from . import views
app_name = 'account'

urlpatterns = [
    path('auth/', views.OtpLoginView.as_view(), name='auth'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('check/', views.CheckOtpView.as_view(), name='check'),
]
