from django.urls import path

from .views import (
    nftcollection_list_view,
    nftcollection_detail_view,
    nftcollection_create_view,
    nftcollection_delete_view,
    nftcollection_update_view,
    nftcollection_detail_hx_view,
    nft_update_hx_view,
    nft_delete_view,
    nftcollection_single_view
)

app_name='nftcollections'

urlpatterns = [
    path("", nftcollection_list_view, name='list'),
    path("create/", nftcollection_create_view, name='create'),

    path("hx/<int:parent_id>/nft/<int:id>/", nft_update_hx_view, name='hx-nft-detail'),
    path("hx/<int:parent_id>/nft/", nft_update_hx_view, name='hx-nft-create'),
    path("hx/<int:id>/", nftcollection_detail_hx_view, name='hx-detail'),

    path("<int:parent_id>/nft/<int:id>/delete/", nft_delete_view, name='nft-delete'),
    path("<int:id>/delete/", nftcollection_delete_view, name='delete'),
    path("<int:id>/edit/", nftcollection_update_view, name='update'),
    path("<int:id>/", nftcollection_detail_view, name='detail'),
    
    path("<slug:slug>/", nftcollection_single_view, name='single-collection'),
]
