from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('topics', views.TopicViewSet)
router.register('resources', views.ResourceViewSet)
router.register('positions', views.PositionViewSet)
router.register('publishers', views.PublisherViewSet)
