from rest_framework import serializers
from django.contrib.auth.models import User

class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email','username','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(username=validated_data["username"],email=validated_data["email"])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'email','username','first_name',"last_name"]
        extra_kwargs = {'id':{"read_only":True}}