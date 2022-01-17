from django.urls import path

from .views import (
    drop_search_view,
    drop_create_view,
    drop_detail_view
)

app_name = 'drops'
urlpatterns = [
    path('', drop_search_view, name='search'),
    path('create/', drop_create_view, name='create'),
    path('<slug:slug>/', drop_detail_view, name='detail'),
]
