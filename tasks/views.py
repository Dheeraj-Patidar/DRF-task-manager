from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import CustomUser, Task
from .serializers import CustomUserSerializer, TaskSerializer


class CustomUserListView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]


class CustomUserRetrieveView(RetrieveAPIView):
    """Retrieve a specific user"""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserUpdateView(UpdateAPIView):
    """Update user details."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserDistroyView(DestroyAPIView):
    """Delete user."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


"""Task API ........................................."""


class TaskListAPIView(ListAPIView):
    """list all tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TaskCreateAPIView(CreateAPIView):
    """create tasks"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    """Assign the currently authenticated user to the 'assigned_to' field."""

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)  # Assign the authenticated user


class TaskRetrieveAPIView(RetrieveAPIView):
    """retrieve single task"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TaskUpdateAPIView(UpdateAPIView):
    """update task"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class TaskDestroyAPIView(DestroyAPIView):
    """delete task"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
