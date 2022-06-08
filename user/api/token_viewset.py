from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class LoginObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attr):

        data = super().validate(attr)
        token = self.get_token(self.user)
        data['id'] = self.user.id
        data['type_user'] = self.user.type_user
        data['success'] = True
        return data

class LoginViewSet(TokenObtainPairView):
    serializer_class = LoginObtainPairSerializer
