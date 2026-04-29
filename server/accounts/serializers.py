from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, ModelSerializer, ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(ModelSerializer):
    password1 = CharField(write_only=True)
    password2 = CharField(write_only=True)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise ValidationError('Passwords must match.')
        return data

    def create(self, validated_data):
        data = {
            key: value for key, value in validated_data.items()
            if key not in ('password1', 'password2')
        }
        data['password'] = validated_data['password2']
        return self.Meta.model.objects.create_user(**data)

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
        )
        read_only_fields = ('id',)


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_data = UserSerializer(user).data
        for key, value in user_data.items():
            if key != 'id':
                token[key] = value
        return token
