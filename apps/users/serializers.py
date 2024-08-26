from django.contrib.auth import get_user_model
from rest_framework import serializers, viewsets, status
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
import django.contrib.auth.password_validation as validations
from django.contrib.auth.hashers import make_password
from django.conf import settings
from djoser.serializers import UserCreateSerializer

User = get_user_model()


class CreateUserSerializer(UserCreateSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        password = data.pop("password")
        password_confirmation = data.pop("password_confirmation")

        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password_confirmation": "Passwords do not match"}
            )

        try:
            validations.validate_password(password=password)

        except ValidationError as err:
            raise serializers.ValidationError({"password": err.messages})

        data["password"] = make_password(password)
        return data

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password",
            "password_confirmation",
            "roles",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if validated_data.get("is_superuser", False):
            user.is_superuser = True
            user.is_staff = True
            user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(source="get_full_name")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "full_name",
            "phone_number",
            "roles",
        ]

    def get_full_name(self, obj):
        return obj.get_full_name

    # def to_representation(self, instance):
    #     representation = super(UserSerializer, self).to_representation(instance)
    #     if instance.is_superuser:
    #         representation["superuser"] = True
    #     return representation

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            user_role=validated_data["user_role"],
            password=validated_data["password"],
        )
        return user


class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField(read_only=True)
    token_class = RefreshToken

    def validate(self, attrs):
        refresh = self.token_class(attrs["refresh"])

        data = {"access": str(refresh.access_token)}
        if settings.SIMPLE_JWT.get("ROTATE_REFRESH_TOKENS"):
            if settings.SIMPLE_JWT.get("BLACKLIST_AFTER_ROTATION"):
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()
            refresh.set_iat()

            data["refresh"] = str(refresh)

        return data
