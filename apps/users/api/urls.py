''' from urllib.parse import urlparse
from django.urls import path


urlpatterns = [
    path('users/', user_api_view ,name = 'usuario_api'),
    path('users/<int:pk>',user_detail_api_view,name='usuario_detail_api_view')
] '''