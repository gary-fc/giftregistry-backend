import os

from django.contrib.auth.hashers import make_password
from rest_framework import serializers, viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserLimitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.is_valid(raise_exception=True))
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # SUCCESS
        username = request.data['username']
        os.mkdir('media/' + username)
        os.mkdir('media/' + username + '/' + 'profile')
        os.mkdir('media/' + username + '/' + 'campaigns')
        return Response({"success": True, "status": status.HTTP_201_CREATED}, status=status.HTTP_201_CREATED,
                        headers=headers)

    @action(methods=['POST'], detail=False, url_path="update-user", url_name="actualizar usuario")
    def update_user_data(self, request):
        id = request.data['id']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email = request.data['email']
        phone = request.data['phone']
        direction = request.data['direction']
        bank_name = request.data['bank_name']
        account_number = request.data['account_number']
        type_account = request.data['type_account']
        tigomoney_number = request.data['tigomoney_number']
        ci = request.data['ci']
        User.objects.all().filter(id=id).update(first_name=first_name, last_name=last_name, email=email,
                                                phone=phone, direction=direction, bank_name=bank_name,
                                                account_number=account_number, type_account=type_account,
                                                tigomoney_number=tigomoney_number, ci=ci)
        return Response("success")
