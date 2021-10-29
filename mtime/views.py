from django.http import JsonResponse, FileResponse
from django.shortcuts import render
from .api_request import request_api

from django.conf import settings


def index(request):
    city = request.GET.get('city')
    data = request_api(city)

    return JsonResponse(data)


def book_view(request, book):
    return render(request, f'{book}/index.html', {'book': book})


def book_img_view(request, book, file):
    return FileResponse(open(str(settings.BASE_DIR) + '\static\\' + book + '\\' + file, 'rb'))


def book_fil_view(request, book, folder, file):
    return FileResponse(open(str(settings.BASE_DIR) + '\static\\' + book + '\\' + folder + '\\' + file, 'rb'))


def book_file_view(request, book, cat, folder, file):
    return FileResponse(open(str(settings.BASE_DIR) + '\static\\' + book + '\\' + cat + '\\' + folder + '\\' + file, 'rb'))