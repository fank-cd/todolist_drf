# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import serializers
from items.models import Todo


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('url',"id", "username", "password")


class UserSerializer(serializers.HyperlinkedModelSerializer):

    Todo = serializers.HyperlinkedRelatedField(many=True, view_name="todo-detail", read_only=True)

    class Meta:
        model = User
        fields = ('url', "id", "username", "Todo", "date_joined")
