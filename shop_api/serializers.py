from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)
from shop_product.api.serializers import CommentSerializer
from shop_product.models import *
from shop_account.models import *
from .models import *


class ProductSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='api:detail',
        lookup_field='pk'
    )
    image = SerializerMethodField()
    class Meta:
        model = Product
        exclude = ('visit_count', 'favourite', 'sell')
    
    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            return None
        return image

class UserSerializer(ModelSerializer):
    user = SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'
    
    def get_user(self, obj):
        return obj.email