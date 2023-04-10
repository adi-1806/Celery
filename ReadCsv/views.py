from rest_framework.views import APIView
from ReadCsv.models import StudentData
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser
from ReadCsv.serializers import CsvDataSerializer
from ReadCsv.task import create_user_profiles

class CreateUserProfilesView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    details = StudentData.objects.all()
    
    def post(self, request):
        serializer = CsvDataSerializer(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            csv_file = request.FILES['file'] 
            create_user_profiles.delay()                  
            return HttpResponse(status=200)
