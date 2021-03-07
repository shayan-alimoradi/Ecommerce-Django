from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from shop_product.models import *


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'product',
            'comment',
            'status',
            'reply',
            'is_reply',
            'reply_count',
        )
    
    def get_reply_count(self, obj):
        if obj.reply:
            return obj.children().count()
        return 0


class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'reply',
        )


class CommentDetailSerializer(ModelSerializer):
    # reply = SerializerMethodField()
    reply_count = SerializerMethodField()
    class Meta:
        model = Comment
        fields = (
            'id',
            'user',
            'product',
            'comment',
            'status',
            'reply',
            'is_reply',
            'reply_count',
        )
    def get_reply_count(self, obj):
        if obj.is_reply:
            return obj.children().count()
        return 0

    # def get_replies(self, obj):
    #     if obj.is_reply:
    #         return CommentChildSerializer(obj.reply, many=True).data
    #     return None