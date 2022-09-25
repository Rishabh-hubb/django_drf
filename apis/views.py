from .serializers import UserSerializers,UserCreateSerializer
from django.contrib.auth.models import User

# Create your views here.
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializers

class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

#class UserUpdate(UpdateAPIView):
#    queryset = User.objects.all()
#    serializer_class = UserUpdateSerializers



class UserExtraView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

