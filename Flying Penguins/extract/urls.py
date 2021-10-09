from django.urls import path

from extract import views

urlpatterns = [
    path('', views.showHTML, name='showHTML'),
    path('extracted/', views.extracted, name='extracted'),

]
