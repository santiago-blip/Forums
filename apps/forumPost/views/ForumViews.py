from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.forumPost.models import (Forum,Gallery)
from apps.forumPost.serializers.ForumSerializer import (ForumPostSerializer,ForumGetSerializer)
from apps.forumPost.serializers.GallerySerializer import GallerytoPostSerializer
from apps.forumPost.pagination import defaultPagination
from apps.forumPost.permissions import ValidUserOfPostUpdate

from django.shortcuts import get_object_or_404
import copy

class ForumView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,ValidUserOfPostUpdate]

    paginator = defaultPagination()

    def get_object(self, pk):
        forum = get_object_or_404(Forum, pk=pk)
        self.check_object_permissions(self.request, forum)
        return forum
    
    def get(self,request, id = None,*args,**kwargs):
        if id:
            query = get_object_or_404(Forum,id=id)
            # breakpoint()
            data = ForumGetSerializer(query)
            return Response(data.data,status=status.HTTP_200_OK)
        query = Forum.objects.all().order_by('id')
        data = self.paginator.paginate_queryset(query,request)
        data = ForumGetSerializer(data,many=True)
        return self.paginator.get_paginated_response(data.data)
        # 
        # return Response(data.data,status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        rawData = copy.deepcopy(request.data)
        rawData['user'] = request.user.id
        galleryData = None
        if rawData.get('image',None) and rawData.get('principal',None):
            galleryData = {}
            galleryData.update({"image":rawData.pop("image")[0]})
            galleryData.update({"principal":bool(rawData.pop("principal"))})
        elif rawData.get('image',None):
            galleryData = {"image":rawData.pop("image")[0]}

        data = ForumPostSerializer(data=rawData)
        data.is_valid(raise_exception=True)
        data = data.save()
        if galleryData:
            galleryData['forum'] = data.id
            serializerGallery = GallerytoPostSerializer(data=galleryData)
            if serializerGallery.is_valid():
                serializerGallery.save()
            else:
                data.delete()
                return Response({"error":serializerGallery.errors},status.HTTP_201_CREATED)
        return Response({"response":"Object created."},status.HTTP_201_CREATED)
    
    def put(self,request,id = None,*args,**kwargs):
        if not id: return Response({"error":"No id given."},status=status.HTTP_400_BAD_REQUEST)
        
        queryInstance = self.get_object(id)
        rawData = copy.deepcopy(request.data)
        rawData['user'] = request.user.id
        galleryData = None
        if rawData.get('image',None) and rawData.get('principal',None):
            galleryData = {}
            galleryData.update({"image":rawData.pop("image")[0]})
            galleryData.update({"principal":bool(rawData.pop("principal"))})
        elif rawData.get('image',None):
            galleryData = {"image":rawData.pop("image")[0]}

        data = ForumPostSerializer(instance=queryInstance,data=rawData)
        data.is_valid(raise_exception=True)
        data = data.save()
        if galleryData:
            galleryData['forum'] = data.id
            serializerGallery = GallerytoPostSerializer(data=galleryData)
            if serializerGallery.is_valid():
                if galleryData.get('principal'):
                    find_principal = Gallery.objects.filter(principal=True).first()
                    if find_principal:
                        find_principal.principal = False
                        find_principal.save()
                serializerGallery.save()
            else:
                data.delete()
                return Response({"error":serializerGallery.errors},status.HTTP_200_OK)
        return Response({"response":"Object updated."},status.HTTP_200_OK)

    def delete(self,request, id = None,*args,**kwargs):
        if not id: return Response({"error":"No id given."},status=status.HTTP_400_BAD_REQUEST)
        
        instance =  self.get_object(id)
        instance.delete()
        return Response({"response":"Object deleted."},status.HTTP_200_OK)
