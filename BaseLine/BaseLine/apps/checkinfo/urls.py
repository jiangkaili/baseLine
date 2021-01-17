# @Author  : jkl
# @Email   : 189156395@qq.com
# @Time    : 2020/12/25 10:41 上午
# @File    : urls.py


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index$', views.Index),
    url(r'^findAll$', views.FindAll.as_view()),
    url(r'^getAllData$', views.GetAllData),
]
