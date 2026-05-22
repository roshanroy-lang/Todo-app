from django.shortcuts import render
from .models import table
from .serializers import task_serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def get_tasks(request):
    a=table.objects.all()
    b=task_serializer(a,many=True)
    return Response(b.data)


