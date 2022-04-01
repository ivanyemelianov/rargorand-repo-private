from django.urls import path

from .views import (
    collection_list_view,
    collection_detail_view,
    collection_create_view,
    collection_update_view,
    collection_delete_view,
    nnft_detail_view,
    nnft_delete_view,
    nnft_create_view,
    nnft_update_view,
    nnft_detail_hx_view,
    ncollection_single_view,
    g_collection_list_view,
    nnft_attribute_delete_view,
    nnft_attribute_update_hx_view
)

app_name = 'ncollections'

urlpatterns = [
    path("", collection_list_view, name="list"),
    path("collection/create/", collection_create_view, name="create"),
    path("<int:id>/delete/", collection_delete_view, name="delete"),
    path("<int:id>/edit/", collection_update_view, name="update"),
    path("<int:id>/", collection_detail_view, name="detail"),

    path("<int:collection_id>/nft/<int:parent_id>/attribute/<int:id>/delete/", nnft_attribute_delete_view, name="attribute-delete"),
    path("hx/nft/<int:parent_id>/attribute/<int:id>", nnft_attribute_update_hx_view, name="hx-attribute-detail"),
    path("hx/nft/<int:parent_id>/attribute/", nnft_attribute_update_hx_view, name="hx-attribute-create"),
    path("<int:parent_id>/nft/create/", nnft_create_view, name="nft-create"),
    path("hx/<int:parent_id>/nft/<int:id>/", nnft_detail_hx_view, name="hx-nft-detail"),
    path("<int:parent_id>/nft/<int:id>/delete/", nnft_delete_view, name="nft-delete"),
    path("<int:parent_id>/nft/<int:id>/edit/", nnft_update_view, name="nft-update"),
    path("<int:parent_id>/nft/<int:id>/", nnft_detail_view, name="nft-detail"),

    path('all/', g_collection_list_view, name='collections'),
    path("<slug:slug>/<int:id>/", ncollection_single_view, name='single-collection'),
]