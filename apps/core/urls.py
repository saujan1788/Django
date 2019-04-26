from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('subnet/', views.SubnetView.as_view(), name='subnet'),
]
