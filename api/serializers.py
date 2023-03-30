from rest_framework import serializers
from database.models import Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    # profile serializer to turn a model's fields into json
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ["user"]
