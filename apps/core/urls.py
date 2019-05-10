from django.urls import path

from apps.core import views

urlpatterns = [
    path(
        '',
        views.HomePageView.as_view(),
        name='home'
    ),
    path(
        'subnet/',
        views.SubnetView.as_view(),
        name='subnet'
    ),
    path(
        'convert/',
        views.ConvertView.as_view(),
        name='convert',
    ),
    path(
        'valid/',
        views.Valid_IPv6View.as_view(),
        name='valid',
    ),

    path(
        'expand/',
        views.ExpandView.as_view(),
        name='expand',
    )
]
