from django.urls import path

from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('records/', views.RecordsView.as_view(), name='records'),
    path('generate/', views.GenerateView.as_view(), name='generate'),
    path('entry/', views.EntryView.as_view(), name='entry'),
    path('customer/', views.AddCustomerView.as_view(), name='customer'),
    path('milk/', views.AddMilkView.as_view(), name='milk'),
]
