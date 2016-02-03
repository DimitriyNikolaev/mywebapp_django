from django.conf.urls import url

urlpatterns = [
    url(r'^category/(?P<group>\d+)$', 'store.views.main_page_filtered'),
    url(r'^about/$', 'store.views.about_page'),
    url(r'^all/$', 'store.views.main_page'),
    url(r'^', 'store.views.main_page')
]