"""todolist_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from items import views as items_view
from users import views as user_view

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += [
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^$', items_view.api_root),
    url(r'^items/$', items_view.TodoList.as_view(), name="todo-list"),
    url(r'^items/(?P<pk>[0-9]+)$', items_view.TodoDetail.as_view(), name="todo-detail"),
]

urlpatterns += [
    url(r'^users/$', user_view.UserListCreate.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_view.UserDetail.as_view(), name='user-detail'),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls')),
]