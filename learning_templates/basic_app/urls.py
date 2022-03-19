from django.conf.urls import url
from basic_app import views

#----tempate tagging---#
app_name = 'basic_app'

urlpatterns = [
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
"""from django.conf.urls import url
from basic_app import views

# SET THE NAMESPACE!
app_name = 'basic_app'

urlpatterns=[
    url(r'^relative/$', views.relative,name='relative'),
    url(r'^other/$', views.other,name='other'),
]
"""