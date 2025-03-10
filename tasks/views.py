from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
# from django.http import Http404.
from .models import CustomUser, Task
from .serializers import CustomUserSerializer, TaskSerializer


class UserListCreatAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """get all the users"""
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        """create a user"""
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserListUpdateDelete(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """get user"""
        return get_object_or_404(CustomUser, pk=pk)

    def get(self, request, pk):
        """get single user with id"""
        user = self.get_object(pk)
        if user is None:
            return Response(
                {"error": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """update user"""
        user = self.get_object(pk)
        if user is None:
            return Response(
                {"error": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = CustomUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """delete user with id"""
        user = self.get_object(pk)
        if user is None:
            return Response(
                {"error": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response(
            {"massage": "user deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class TaskListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """"get all the tasks"""
        tasks = Task.objects.all()
        status_filter = request.query_params.get("status")
        if status_filter:
            tasks = tasks.filter(status=status_filter)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        """create a task"""
        serializer = TaskSerializer(data=request.data, context={"request": request})
        if serializer.is_valid(raise_exception=True): # this should be included or not
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """get task"""
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        """get task with id"""
        task = self.get_object(pk)
        if task is None:
            return Response(
                {"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        """update task"""
        task = self.get_object(pk)
        if task is None:
            return Response(
                {"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """delete task"""
        task = self.get_object(pk)
        if task is None:
            return Response(
                {"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND
            )
        task.delete()
        return Response({"message": "Task deleted"}, status=status.HTTP_204_NO_CONTENT)


# JWT Authentication Views
class ObtainTokenView(APIView):
    """obtain access token for authentication"""
    def post(self, request):
        user = CustomUser.objects.filter(email=request.data.get("email")).first()
        if user and user.check_password(request.data.get("password")):
            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)}
            )
        return Response(
            {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class RefreshTokenView(APIView):
    """obtain access token again from refresh token"""
    def post(self, request):
        refresh = request.data.get("refresh")
        if not refresh:
            return Response(
                {"error": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            new_token = RefreshToken(refresh).access_token
            return Response({"access": str(new_token)})
        except Exception:
            return Response(
                {"error": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED
            )


# class TaskAPIView(APIView):
#     def get(self, request):
#         task = Task.objects.all()
#         serializer = TaskSerializer(task, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


# class TaskDetailAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         task = self.get_object(pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer)
#         return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

#     def delete(self, request, pk):
#         task =self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
