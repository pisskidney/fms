from builder import views
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'signup/$', views.SignupView.as_view(), name='signup'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
)
