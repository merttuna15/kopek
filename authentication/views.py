from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.views import TokenViewBase
from authentication.serializers import UserSerializer
from kopek2.api.views import BaseViewSet
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




