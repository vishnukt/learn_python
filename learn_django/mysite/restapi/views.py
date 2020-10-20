from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from restapi.api import UserSerializer, GroupSerializer, UserModel
from rest_framework.views import APIView
from user_data.models import user_data


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDataView(viewsets.ModelViewSet):
    queryset = user_data.objects.all()
    serializer_class = UserModel
    permission_classes = [permissions.IsAuthenticated]


# class UserDataView(viewsets.ModelViewSet):
#     serializer_class = UserModel
#     permission_classes = [permissions.IsAuthenticated]

# class UserDataView(APIView):
#     serializer_class = UserModel

#     def get(self, request, format=None):
#         mess = "Hello"
#         return Response({'mess': mess})

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('fullname')
#             message = f'Hello {name}!'
#             return Response({'message': message})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )

