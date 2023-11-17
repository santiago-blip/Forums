from rest_framework import serializers
from apps.forumPost.models import Forum
from apps.user.serializers.userSerializer import UserGetSimpleSerializer
from apps.forumPost.serializers.GallerySerializer import GallerytoShowForumSerializer
from apps.forumPost.serializers.CommentsSerializer import CommentSerializer,CommentWithResponseSerializer

class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ForumGetSerializer(serializers.ModelSerializer):
    user = UserGetSimpleSerializer(read_only=True)
    # gallery_set = GallerytoShowForumSerializer(many=True,read_only=True)
    gallery = GallerytoShowForumSerializer(many=True, read_only=True, source='gallery_set')
    comments = CommentWithResponseSerializer(many=True,read_only=True, source='comment_set')
    class Meta:
        model = Forum
        fields = (
            'id','user','title','description',
            'creation_date','updated_date',
            'likes','dislikes','gallery','comments')