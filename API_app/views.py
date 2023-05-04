from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse
# Create your views here.


def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythonData = JSONParser.parse(stream)
        id = pythonData.get('id', None)
        if id is not None:
            student_data = Student.objects.get(id=id)
            serializer = StudentSerializer(data=student_data)
            json_data = JSONRenderer.render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        else:
            student_data = Student.objects.all()
            serializer = StudentSerializer(student_data, many=True)
            json_data = JSONRenderer.render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
