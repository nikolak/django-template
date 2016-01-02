from . import views
from django.conf.urls import url

urlpatterns = [
    url(
        regex=r'^$',
        view=views.HelloWorld.as_view(),
        name='home'
    ), ]
