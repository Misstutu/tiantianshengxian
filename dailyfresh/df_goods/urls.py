from django.conf.urls import url
import views
urlpatterns=[
    url(r'^$',views.index),
    #url(r'^user_center_info/$',views.user_center_info),
    #url(r'^detail/$',views.detail),
    url(r'^list(\d+)_(\d+)_(\d+)/$', views.list),
    url(r'^add(\d+)/$',views.detail),

]
