from django.conf.urls import url
import views
urlpatterns=[
    url('^add(\d+)_(\d+)/$', views.add),
    url('^list/$', views.list),
    url('^count_change/$',views.count_change),
    url('^delete/$',views.delete),
    url('^order/$',views.order),
]