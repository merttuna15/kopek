from rest_framework.routers import DefaultRouter
from authentication.views import UserViewSet
from rest_framework_simplejwt.views import TokenBlacklistView

router = DefaultRouter()

router.register('register', UserViewSet)

urlpatterns = router.urls
