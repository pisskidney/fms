from builder import views
from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'signup/$', views.SignupView.as_view(), name='signup'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'account/$', login_required(views.AccountView.as_view()), name='account'),
    url(r'api/([0-9a-zA-Z]+)$', views.CheckDomainView.as_view(), name='checkdomain'),
    url(r'build/1$', views.BuildNameView.as_view(), name='build_name'),
    url(r'build/2$', views.BuildHomeView.as_view(), name='build_home'),
)
