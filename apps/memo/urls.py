from django.conf.urls import patterns, url
from apps.memo.views import IndexView, LabelListView, LabelEditView, LabelDeleteView, LabelCreateView

urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='memo_index'),
                       url(r'^tag/$', LabelListView.as_view(), name='memo_label_list'),
                       url(r'^tag/edit/(?P<pk>\d+)/$', LabelEditView.as_view(), name='memo_label_edit'),
                       url(r'^tag/delete/(?P<pk>\d+)/$', LabelDeleteView.as_view(), name='memo_label_delete'),
                       url(r'^tag/create/$', LabelCreateView.as_view(), name='memo_label_create'),
                       )
