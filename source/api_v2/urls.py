from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from api_v2 import views

router = routers.DefaultRouter()

router.register(r'projectss', views.ProductViewSet)
router.register(r'taskss', views.TaskViewSet)

app_name = 'api_v2'

urlpatterns = [

    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')

]