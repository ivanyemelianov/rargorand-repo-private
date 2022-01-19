from django.urls import path

from .views import (
    nftcollection_list_view,
    nftcollection_detail_view,
    nftcollection_create_view,
    nftcollection_update_view,
    nftcollection_detail_hx_view
)

app_name='nftcollections'

urlpatterns = [
    path("", nftcollection_list_view, name='list'),
    path("create/", nftcollection_create_view, name='create'),
    path("hx/<int:id>/", nftcollection_detail_hx_view, name='hx-detail'),
    path("<int:id>/edit/", nftcollection_update_view, name='update'),
    path("<int:id>/", nftcollection_detail_view, name='detail'),
]
