from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','mobile','password')
        extra_kwargs = {'password':{'write_only':True}}
    def create(self, validated_data):
        user = User.objects.create(
            mobile = validated_data['mobile'],
            password = validated_data['password']   
        )
        return user
