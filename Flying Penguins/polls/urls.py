from django.urls import path

from polls import views

urlpatterns = [
    # path('', views.view, name='view'),
    path('', views.detected, name='detected'),

]
