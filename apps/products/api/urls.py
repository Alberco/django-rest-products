from django.urls import path
from apps.products.api.views.general_views import CategoryProductViewSet,IndicatorViewSet,MeasureUnitViewSet
from apps.products.api.views.product_viewsets import ProductListCreateAPIView ,ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('measure_unit/',MeasureUnitViewSet.as_view() ,name = 'measure_unit'),
    path('indicator/',IndicatorViewSet.as_view() ,name = 'indicator'),
    path('category-product/',CategoryProductViewSet.as_view() ,name = 'category_product'),
    path('product/',ProductListCreateAPIView.as_view() ,name = 'product_created'),
    path('product/retrieve-update-destroy/<int:pk>/',ProductRetrieveUpdateDestroyAPIView.as_view() ,name = 'product_retrieve'),
]