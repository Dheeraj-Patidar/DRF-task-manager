from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    CustomUserCreateView,
    CustomUserDistroyView,
    CustomUserListView,
    CustomUserRetrieveView,
    CustomUserUpdateView,
    TaskCreateAPIView,
    TaskDestroyAPIView,
    TaskListAPIView,
    TaskRetrieveAPIView,
    TaskUpdateAPIView,
)

urlpatterns = [
    path("user-list/", CustomUserListView.as_view(), name="user-list"),
    path("user-create/", CustomUserCreateView.as_view(), name="user-create"),
    path(
        "user-retriev/<int:pk>/", CustomUserRetrieveView.as_view(), name="retrieve-user"
    ),
    path("user-update/<int:pk>/", CustomUserUpdateView.as_view(), name="update-user"),
    path("user-delete/<int:pk>/", CustomUserDistroyView.as_view(), name="delete-user"),
    path("task-list/", TaskListAPIView.as_view(), name="task-list"),
    path("task-create/", TaskCreateAPIView.as_view(), name="task-create"),
    path(
        "task-retrieve/<int:pk>/", TaskRetrieveAPIView.as_view(), name="task-retrieve"
    ),
    path("task-update/<int:pk>/", TaskUpdateAPIView.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDestroyAPIView.as_view(), name="task-delete"),
    path(
        "token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # Get access & refresh tokens
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # Refresh access token
]
