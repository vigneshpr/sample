from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_test, name='index'),
    url(r'^test1/', views.index_test1, name='index'),
    url(r'^test2/', views.index_test2, name='index'),
    url(r'^test3/', views.index_test3, name='index'),
]