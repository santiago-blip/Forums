from rest_framework import serializers
from apps.forumPost.models import Gallery

class GallerytoShowForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ('id','principal','image')

class GallerytoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'
