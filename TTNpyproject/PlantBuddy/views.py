from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from PlantBuddy.models import DeviceModel


# Create your views here.
class index(APIView):
    queryset = DeviceModel.objects.all()

    def get(self, request):
        return Response({"message": "Welcome"}, status=status.HTTP_200_OK)
