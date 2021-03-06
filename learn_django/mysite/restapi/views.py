# from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.response import Response
from restapi.api import UserSerializer, GroupSerializer, UserModelSerializer
from rest_framework.views import APIView
from user_data.models import user_data
from rest_framework.authentication import TokenAuthentication
# from restapi import token_permissions
# from rest_framework.authtoken.views import ObtainAuthToken


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
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (token_permissions.UpdateOwnProfile, )
    queryset = user_data.objects.all()
    # queryset = user_data.objects.filter(user = request.user)
    serializer_class = UserModelSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            n = serializer.validated_data.get('full_name')
            t = serializer.validated_data.get('home_town')
            a = serializer.validated_data.get('age')
            u = user_data(full_name=n, home_town=t, age=a)
            u.user = request.user
            u.save()
            message = f'{u.user} Data Succesfully Saved!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # def retrieve(self, request, pk=None):
    #     pass

    def update(self, request, pk=None):
        """Handle updating an object"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            n = serializer.validated_data.get('full_name')
            t = serializer.validated_data.get('home_town')
            a = serializer.validated_data.get('age')
            # u = user_data(full_name=n, home_town=t, age=a)
            user_data.objects.filter(id=pk).update(full_name=n, home_town=t, age=a)
            message = 'Data Succesfully Updated!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    # def partial_update(self, request, pk=None):
    #     return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        user_data.objects.filter(id=pk).delete()
        return Response({'SUCCESSFULLY DELETE'})


class UserDataApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)
    queryset = user_data.objects.all()
    serializer_class = UserModelSerializer

    def get(self, request, format=None, pk=None):
        queryset = user_data.objects.all()
        serializer_class = UserModelSerializer(queryset, many=True)
        return Response(serializer_class.data)
        # if pk is None:
        #     return Response({self.queryset.all()})
        # else:
        #     return Response({self.queryset.filter(pk=pk)})

    def post(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            n = serializer.validated_data.get('full_name')
            t = serializer.validated_data.get('home_town')
            a = serializer.validated_data.get('age')
            u = user_data(full_name=n, home_town=t, age=a)
            u.user = request.user
            u.save()
            message = f'{u.user} Data Succesfully Saved!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserDataPutApiView(APIView):
    queryset = user_data.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    # permission_classes = (token_permissions.UpdateOwnProfile,)

    def get(self, request, format=None, pk=None):
        queryset = user_data.objects.filter(pk=pk)
        serializer_class = UserModelSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            n = serializer.validated_data.get('full_name')
            t = serializer.validated_data.get('home_town')
            a = serializer.validated_data.get('age')
            # u = user_data(full_name=n, home_town=t, age=a)
            user_data.objects.filter(id=pk).update(full_name=n, home_town=t, age=a)
            message = 'Data Succesfully Updated!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            n = serializer.validated_data.get('full_name')
            t = serializer.validated_data.get('home_town')
            a = serializer.validated_data.get('age')
            # u = user_data(full_name=n, home_town=t, age=a)
            if n is None:
                n = self.queryset.filter(pk=pk).values('full_name')
            if t is None:
                t = self.queryset.filter(pk=pk).values('home_town')
            if a is None:
                a = self.queryset.filter(pk=pk).values('age')
            user_data.objects.filter(id=pk).update(full_name=n, home_town=t, age=a)
            message = 'Data Succesfully Updated!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        user_data.objects.filter(id=pk).delete()
        return Response({'SUCCESSFULLY DELETE'})


# class UserLoginApiView(ObtainAuthToken):
#    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
