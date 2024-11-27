from django.urls import path
from . import views
from .views import news_list, news_detail, indexView ,ContactsView , nimadir, ContactSend,ichiga

urlpatterns = [
    path("", indexView, name="indexView"), 
    path("all/", news_list, name="all_news_list"), 
    path("<int:id>/", news_detail, name="news_detail_page"),
    path("contacts/", ContactsView, name="contacts"),
    path("nimadir/", nimadir, name="nimadir"),
    path("ContactSend", ContactSend, name="ContactSend"),
    path("ichiga", ichiga, name="ichiga"),

]