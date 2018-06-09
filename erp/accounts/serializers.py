from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializes user profile objects.
    """

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Create new user
        """
        user = UserProfile(
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
