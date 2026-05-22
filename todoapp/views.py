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
@api_view(['POST'])
def post_tasks(request):
    a=task_serializer(data=request.data)
    if a.is_valid():
        a.save()
        return Response(a.data)
    else:
        return Response(a.errors)
    