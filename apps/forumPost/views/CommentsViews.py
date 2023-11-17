from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.forumPost.models import (Forum,Comment)
from apps.forumPost.serializers.CommentsSerializer import CommentSerializer

import copy


class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request,*args,**kwargs):
        rawData = copy.deepcopy(request.data)
        rawData['user'] = request.user.id
        # breakpoint()
        data = CommentSerializer(data=rawData)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({"response":"Object has been created."},status=status.HTTP_201_CREATED)

