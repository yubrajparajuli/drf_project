from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'username', 'password', 'membership_type', 'membership_start_date', 'membership_expiry_date']
        read_only_fields = ['membership_start_date', 'membership_expiry_date']

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data['phone_number'],
            username=validated_data.get('username', ''),
            password=validated_data['password'],
            membership_type=validated_data.get('membership_type')
        )
        return user
