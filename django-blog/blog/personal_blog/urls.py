from django.conf.urls import url
import views


urlpatterns=[
    # url(r'$',views.)
    url(r'^detail/(?P<article_id>\d+)/$',views.detail,name='article_detail'),
    url(r'^recommend/(?P<recommend_id>\d+)/$',views.recommend,name='recommend_detail'),
    url(r'^list/(?P<column_id>\d+)/$',views.list,name='list')
]