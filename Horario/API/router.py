from rest_framework.routers import DefaultRouter
from Horario.API.views import *

router_posts=DefaultRouter()
router_posts.register(prefix='post',basename='post',viewset=ProfesorApiViewSet)
