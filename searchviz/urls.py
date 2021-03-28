from django.conf.urls import url
from .api import SearchAPI

urlpatterns = [
    url(r'^searchName$', SearchAPI.as_view())
]
