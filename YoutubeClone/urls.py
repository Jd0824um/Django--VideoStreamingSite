from django.contrib import admin
from django.conf.urls import url, include
from YoutubeClone import views

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('accounts.urls'))
]
