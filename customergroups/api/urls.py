from django.conf.urls import url
from django.urls import path

from .views import CustomerGroupAPIView, CustomerGroupAPIDetailView, CustomerGroupReadAPIView


app_name = "api-group"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('create/', CustomerGroupAPIView.as_view(), name='list-create'),
    url(r'^(?P<id>\d+)/$', CustomerGroupAPIDetailView.as_view(), name='detail'),
    path('', CustomerGroupReadAPIView.as_view(), name='list')
]