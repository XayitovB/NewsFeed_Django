from django.shortcuts import render, get_object_or_404
from .form import ContactForm
from django.http import HttpResponse
from .models import News, Category
# Create your views here.


def news_list(request):
    news_list = News.objects.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)
def news_detail(request, id):
    news = get_object_or_404(News, id = id)
    context = {
        "news": news
    }
    return render(request, "news/news_detail.html", context)

def indexView(request):
    news = News.objects.all().order_by("-publish_time")[:5]
    categories_list = Category.objects.all()
    iqtisodList = News.objects.all().filter(category_id__name="Iqtisodiyot").order_by("-publish_time")[1:5]
    iqtisodList_one = News.objects.all().filter(category_id__name="Iqtisodiyot").order_by("-publish_time")[0]
    
    uzbekistonList = News.objects.all().filter(category_id__name="Uzbekiston").order_by("-publish_time")[1:5]
    uzbekiston_one = News.objects.all().filter(category_id__name="Uzbekiston").order_by("-publish_time")[0]


    jahonList = News.objects.all().filter(category_id__name="Jahon").order_by("-publish_time")[1:5]
    jahon_one = News.objects.all().filter(category_id__name="Jahon").order_by("-publish_time")[0]



    context = {
        "news": news,
        "categories_list": categories_list,
        "iqtisodList": iqtisodList,
        "iqtisodList_one": iqtisodList_one,
        "uzbekistonList": uzbekistonList,
        "uzbekiston_one": uzbekiston_one,
        "jahonList ": jahonList,
        "jahon_one ": jahon_one,
    }

    return render(request, "news/index.html", context)
def ContactsView(request):
    return render(request, "news/contact.html")
def ichiga(request):
    context = {
        "news": News.objects.get(pk = news)
    }
def nimadir(request):
    return render(request, "news/404.html")


def ContactSend(request):
    form = ContactForm(request.POST)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Zoooooor</h1>")