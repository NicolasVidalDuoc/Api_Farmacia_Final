from django.contrib.auth.models import User, Group
from rest_framework import serializers
from productosFarmacia.models import Productos


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['url', 'id_producto', 'nombre_producto', 'stock_producto']