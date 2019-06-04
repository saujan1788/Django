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
        'info/',
        views.GeneralInfoView.as_view(),
        name='general-info',
    ),
    path(
        'mac/',
        views.MacAddressView.as_view(),
        name='mac-address',
    ),
    path(
        'valid/',
        views.ValidIPv6View.as_view(),
        name='valid',
    ),

    path(
        'expand/',
        views.ExpandView.as_view(),
        name='expand',
    )
]
