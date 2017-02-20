from django.conf.urls import url
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^$', views.RestrictedView.as_view()),
]
