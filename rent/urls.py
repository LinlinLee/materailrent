from django.conf.urls import url
from rent import views

urlpatterns = [
    url(r'^$', 'rent.views.rent_index', name='rent_index'),
    url(r'^login', 'rent.views.login', name='login'),
 
]
