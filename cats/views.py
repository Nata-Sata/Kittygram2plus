from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle
# from rest_framework.pagination import LimitOffsetPagination

from .models import Achievement, Cat, User
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .pagination import CatsPagination
from .permissions import OwnerOrReadOnly
from .throttling import WorkingHoursThrottle

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    throttle_classes = (AnonRateThrottle, WorkingHoursThrottle, ScopedRateThrottle)
    throttle_scope = 'low_request'
    pagination_class = CatsPagination

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer