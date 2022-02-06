from django.urls import path

from .views import (
    drop_search_view,
    drop_create_view,
    drop_detail_view,
    drop_list_view,
    drop_update_view,
    drop_delete_view,
    drop_detail_hx_view,
    drop_single_view
)

app_name = 'drops'
urlpatterns = [
    path('', drop_list_view, name='list'),
    #path('', drop_search_view, name='search'),
    path('create/', drop_create_view, name='create'),

    path("hx/<int:id>/", drop_detail_hx_view, name='hx-detail'),

    path("<int:id>/delete/", drop_delete_view, name='delete'),
    path("<int:id>/edit/", drop_update_view, name='update'),
    path("<int:id>/", drop_detail_view, name='detail'),

    path('<slug:slug>/', drop_single_view, name='single'),
]
