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
    """showing all users"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class CustomUserCreateView(CreateAPIView):
    """create new user"""
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


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

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)
    

class CustomUserDistroyView(DestroyAPIView):
    """Delete only the logged-in user's account."""

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

"""Task API ..................................................................................."""


class TaskListAPIView(ListAPIView):
    """List tasks assigned to the logged-in user"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskCreateAPIView(CreateAPIView):
    """Create a new task and assign it to the logged-in user"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    """Assign the currently authenticated user to the 'assigned_to' field."""

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)  # Assign the authenticated user


class TaskRetrieveAPIView(RetrieveAPIView):
    """Retrieve only tasks assigned to the logged-in user"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskUpdateAPIView(UpdateAPIView):
    """Update only tasks assigned to the logged-in user"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskDestroyAPIView(DestroyAPIView):
    """Delete only tasks assigned to the logged-in user"""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)
