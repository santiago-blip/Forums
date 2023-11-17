from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.forumPost.models import (Forum,Gallery,LikesDislikeForum,Comment,LikesDislikeForumComment)

import copy

class LikesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        if not request.data.get('forum_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        forumInstance = Forum.objects.get(id=request.data.get('forum_id'))

        instance = LikesDislikeForum.objects.filter(
            user=request.user.id,
            forum = request.data.get('forum_id')
        ).first()
        if not instance:
            LikesDislikeForum.objects.create(
                user=request.user,
                forum = forumInstance,
                like=True
            )
        else:
            if not instance.dislike:
                instance.delete()
            else:
                instance.dislike = False
                instance.like = True
                instance.save()
        #UpdateForo
        forumInstance.save()

        return Response(status=status.HTTP_200_OK)


class DislikesView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        if not request.data.get('forum_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        forumInstance = Forum.objects.get(id=request.data.get('forum_id'))

        instance = LikesDislikeForum.objects.filter(
            user=request.user.id,
            forum = request.data.get('forum_id')
        ).first()
        if not instance:
            LikesDislikeForum.objects.create(
                user=request.user,
                forum = forumInstance,
                dislike=True
            )
        else:
            if not instance.like:
                instance.delete()
            else:
                instance.like = False
                instance.dislike = True
                instance.save()
        #UpdateForo
        forumInstance.save()

        return Response(status=status.HTTP_200_OK)
    
class LikesCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        if not request.data.get('comment_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        commentInstance = Comment.objects.get(id=request.data.get('comment_id'))


        instance = LikesDislikeForumComment.objects.filter(
            user=request.user.id,
            comment = request.data.get('comment_id')
        ).first()
        if not instance:
            LikesDislikeForumComment.objects.create(
                user=request.user,
                comment = commentInstance,
                like=True
            )
        else:
            if not instance.dislike:
                instance.delete()
            else:
                instance.dislike = False
                instance.like = True
                instance.save()
        #UpdateForo
        commentInstance.save()

        return Response(status=status.HTTP_200_OK)


class DislikesCommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):

        if not request.data.get('comment_id'):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        commentInstance = Comment.objects.get(id=request.data.get('comment_id'))


        instance = LikesDislikeForumComment.objects.filter(
            user=request.user.id,
            comment = request.data.get('comment_id')
        ).first()
        if not instance:
            LikesDislikeForumComment.objects.create(
                user=request.user,
                comment = commentInstance,
                dislike=True
            )
        else:
            if not instance.like:
                instance.delete()
            else:
                instance.like = False
                instance.dislike = True
                instance.save()
        #UpdateForo
        commentInstance.save()

        return Response(status=status.HTTP_200_OK)