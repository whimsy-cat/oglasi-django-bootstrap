from rest_framework import routers

from category.views import CategoryViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = router.urls
