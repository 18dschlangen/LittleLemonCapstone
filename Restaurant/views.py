from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def token_auth(request):
    if request.method == 'POST':
        return obtain_auth_token(request)
    else:
        return HttpResponseNotAllowed(['POST'])

class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 