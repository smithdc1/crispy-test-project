"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

from bootstrap.views import index as bootstrap
from bootstrap3.views import index as bootstrap_3_preview
from bootstrap4.views import index as bootstrap_4_preview
from bootstrap4_3.views import index as bootstrap_4_3
from materialize.views import index as materialize
from semantic.views import index as semantic_preview

urlpatterns = [
    url(r'^$', bootstrap_4_preview),
    url(r'^bootstrap3$', bootstrap_3_preview, name='bootstrap3.views.index'),
    url(r'^bootstrap4$', bootstrap_4_preview, name='bootstrap4.views.index'),
    url(r'^bootstrap4_3$', bootstrap_4_3, name='bootstrap4_3.views.index'),
    url(r'^bootstrap$', bootstrap, name='bootstrap.views.index'),
    url(r'^materialize$', materialize, name='materialize.views.index'),
    url(r'^semantic', semantic_preview, name='semantic.views.index'),
]
