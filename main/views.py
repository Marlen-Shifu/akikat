from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.generic import ListView, DetailView

from .models import Article, SubCategory

from mtime.models import City
from mtime.api_request import request_api


def index(request):
    city = request.GET.get('gorod')
    if city:
        data = request_api(city)
    else:
        data = request_api()

    data['city'] = city

    return render(request, 'index.html', data)


class ArticleListView(ListView):
    model = Article
    template_name = 'article-iman.html'
    paginate_by = 2

    def get_queryset(self):
        qs = super().get_queryset()
        subcategory = SubCategory.objects.get(slug = self.kwargs.get('subcategory'))
        qs_to_return = qs.filter(subcategory = subcategory)
        return qs_to_return

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.kwargs.get('category') == self.kwargs.get('subcategory'):
            context["single"] = True
            subcategory = SubCategory.objects.get(slug = self.kwargs.get('subcategory'))
            context["title"] = subcategory.name

        articles = Article.objects.all().order_by('-looks')


        context['tanimal1'] = articles[0]
        context['tanimal2'] = articles[1]
        context['tanimal3'] = articles[2]

        context['kop_karalgandar'] = articles[3:8]

        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article-inside.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        print(obj.body)
        obj.increase_look()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(subcategory__pk = self.object.subcategory.pk).exclude(pk = self.object.pk)[:4]

        context["oki_otiriniz"] = articles

        return context


class SearchPage(ListView):
    template_name = 'article-iman.html'
    model = Article


    def get_queryset(self):
        qs = super().get_queryset()
        print(qs)
        qs = qs.filter(name__icontains = self.request.GET.get('q'))
        print(qs)
        return qs
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchPage, self).get_context_data(object_list=object_list, **kwargs)
        context['single'] = True
        context['title'] = 'Іздеудің нәтижесі'

        articles = Article.objects.all().order_by('-looks')


        context['tanimal1'] = articles[0]
        context['tanimal2'] = articles[1]
        context['tanimal3'] = articles[2]

        context['kop_karalgandar'] = articles[3:8]

        return context


def qasietti_kunder(request):
    return render(request, 'qasietti-kunder.html')


def increase_like(request, pk):
    try:
        obj = Article.objects.get(pk = pk)
        obj.increase_like()
    except Exception as e:
        return JsonResponse({'ok': False, 'error': e})
    return JsonResponse({'ok': True, 'likes_count': obj.likes})