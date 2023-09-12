from rest_framework import routers
from .views import MenuCategoryViewSet, MenuItemViewSet, OrderViewSet

router = routers.DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = router.urls