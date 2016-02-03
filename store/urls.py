from django.conf.urls import url

urlpatterns = [
    url(r'^category/(?P<group>\d+)/page/(?P<page>\d+)/$', 'store.views.main_page'),
    url(r'^about/', 'store.views.about_page'),
    url(r'^', 'store.views.main_page')
]