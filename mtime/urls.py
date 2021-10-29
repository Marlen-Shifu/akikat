from django.urls import path

from .views import index, book_view, book_file_view, book_fil_view, book_img_view

urlpatterns = [
    path('', index),
    path('book/<str:book>/', book_view),
    path('book/<str:book>/<str:file>/', book_img_view),
    path('book/<str:book>/<str:folder>/<str:file>/', book_fil_view),
    path('book/<str:book>/<str:cat>/<str:folder>/<str:file>/', book_file_view),
]
