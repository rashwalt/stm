from django.conf.urls import patterns, url
from .views import IndexView, LabelListView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='memo_index'),
                       url(r'^tag/$', LabelListView.as_view(), name='memo_label_list'),
                       )
