from rest_framework.serializers import (
    ModelSerializer,
    EmailField,
    CharField,
)
from django.core.validators import ValidationError
from django.db.models import Q
from shop_account.models import *
from django import forms


class UserCreateSerializer(ModelSerializer):
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = (
            'username', 
            'email', 
            'email2',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    # def validate(self, data):
    #     username = data['username']
    #     qs = User.objects.filter(username=username)
    #     if qs.exists():
    #         raise ValidationError('this username has already exists')
    #     return data
    
    def validate(self, data):
        email = data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise ValidationError('this email has already exists')
        return data
    
    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get('email')
        email2 = value
        if email1 != email2:
            raise forms.ValidationError('Emails must match')
        return value
    
    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    email = EmailField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = (
            'token',
            'email', 
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def validate(self, data):
        user_obj = None
        email = data.get('email', None)
        password = data['password']
        if not email:
            raise ValidationError('email is required to sign-in')
        user = User.objects.filter(
            Q(email=email) 
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('this email is not valid')
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('incorrect credential, please try again!')
        data['token'] = 'Some Random Token'
        return data