from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^$', views.index),
        url(r'^logout',views.logout),
        url(r'^create',views.create),
        url(r'^add/(?P<quote_id>\d+)', views.add),
        url(r'^remove/(?P<quote_id>\d+)', views.remove),
        url(r'^user/(?P<user_id>\d+)', views.user),
        
]
