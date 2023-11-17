from rest_framework import serializers
from apps.forumPost.models import Comment
from apps.user.serializers.userSerializer import UserGetSimpleSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ResponseSerializer(serializers.ModelSerializer):
    user = UserGetSimpleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'comment',
            'image',
            'creation_date',
            'updated_date',
            'likes',
            'dislikes',
        ]
    

class CommentWithResponseSerializer(serializers.ModelSerializer):
    responses = ResponseSerializer(many=True,read_only=True, source='responses_comment')
    user = UserGetSimpleSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = [
            'id',
            'user',
            'comment',
            'image',
            'response_of',
            'creation_date',
            'updated_date',
            'likes',
            'dislikes',
            'responses',
        ]