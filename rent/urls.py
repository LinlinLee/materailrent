from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'rent.views.rent_index', name='rent_index'),
]
