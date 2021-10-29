from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index, name = 'home'),
    path('increase-like/<int:pk>/', increase_like),
    path('articles/<slug:category>/<slug:subcategory>/', ArticleListView.as_view(), name='sb-articles'),
    path('articles/<slug:category>/<slug:subcategory>/<int:pk>/', ArticleDetailView.as_view(), name='article'),
    path('qasietti-kunder/', qasietti_kunder, name='qasietti_kunder'),
    path('search/', SearchPage.as_view(), name='search'),
]
