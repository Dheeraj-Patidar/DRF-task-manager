from django.urls import path

from .views import (CustomUserListUpdateDelete, ObtainTokenView,
                    RefreshTokenView, TaskDetailAPIView, TaskListCreateAPIView,
                    UserListCreatAPIView)

urlpatterns = [
    path("user/", UserListCreatAPIView.as_view(), name="user_list_create"),
    path(
        "user/<int:pk>/",
        CustomUserListUpdateDelete.as_view(),
        name="user_list_update_delete",
    ),
    path("tasks/", TaskListCreateAPIView.as_view(), name="task_list_create"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task_detail"),
    path("token/", ObtainTokenView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", RefreshTokenView.as_view(), name="token_refresh"),
]
