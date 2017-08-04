from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form-person$', views.form_person, name='form_person'),
    url(r'^form-org$', views.form_org, name='form_org'),
]

