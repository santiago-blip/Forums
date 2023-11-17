from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.user.models import User
from .serializers.userSerializer import UserPostSerializer


class UserView(APIView):

    def post(self,request):
        data = UserPostSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({"response":"User created sucessfully."},status=status.HTTP_201_CREATED)
    
    def get(self,request):
        return Response(UserPostSerializer(User.objects.all(),many=True).data)