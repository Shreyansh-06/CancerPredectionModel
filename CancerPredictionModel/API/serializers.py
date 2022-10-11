from operator import attrgetter
from pyexpat import model
from tkinter.ttk import Style
from xml.dom import ValidationErr
from rest_framework import serializers
from API.models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(Style={'input_type':'password'}, write_only=True)
    class Meta:
        model : User
        fleids = ['email', 'name', 'tc','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

def validate(self, attrs):
    password: attrs.get('password')
    password2: attrs.get('password2')
    if password != password2:
        raise serializers.ValidationError("Password and confrim password doent match")
        return attrs

def create(self, validate_data):
    return User.objects.create_user(**validate_data)




