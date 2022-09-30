from django.urls import path
from . import views

## ここにurlと対応するページを書いていく
## reactのRouterみたいなやつ
urlpatterns = [
    path('', views.index, name='index'), 
]


