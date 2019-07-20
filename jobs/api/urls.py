from django.conf.urls import url
from django.urls import path

from .views import JobAPIView, JobAPIReadView, JobAPIDetailView, GroupAPIDetailView


app_name = "api-jobs"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('create/', JobAPIView.as_view(), name='list-create'),
    url(r'^gr/(?P<group>\d+)/$', GroupAPIDetailView.as_view(), name='g-detail'),
    url(r'^(?P<id>\d+)/$', JobAPIDetailView.as_view(), name='detail'),
    url('', JobAPIReadView.as_view(), name='list'),
]