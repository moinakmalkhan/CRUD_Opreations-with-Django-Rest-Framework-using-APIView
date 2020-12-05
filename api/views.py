from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializer import StudentSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def FunctionBasedStudentAPI(request, pk=None):
    data = request.data
    if pk is None:
        pk = data.get("id", None)
    if request.method == "GET":
        if pk is not None:
            stu = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PUT":
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "PATCH":
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        stu = get_object_or_404(Student, id=pk)
        stu.delete()
        return Response({"msg": "Data successfully deleted"}, status=200)

    return Response({"msg": f"This is {request.method} request. Data not found."}, status=status.HTTP_400_BAD_REQUEST)


class ClassBasedStudentAPI(APIView):

    def get(self, request, pk=None, format=None):
        if pk is not None:
            stu = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data successfully Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stu = get_object_or_404(Student, id=pk)
        stu.delete()
        return Response({"msg": "Data successfully deleted"}, status=200)
