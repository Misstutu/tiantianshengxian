from django.conf.urls import url
from . import views
urlpatterns=[

    url(r'^register/$',views.register),
    url(r'^post1/$',views.post1),
    url(r'^post2/$',views.denglu),
    url(r'^login/$',views.login),
    url(r'^cart/$',views.cart),
    url(r'^detail/$',views.detail),
    url(r'^list/$', views.list),
    url(r'^place_order/$', views.place_order),
    url(r'^user_center_info/$',views.user_center_info),
    url(r'^user_center_order/$', views.user_center_order),
    url(r'^user_center_site/$', views.user_center_site),
    url(r'^logout/$',views.logout),

]