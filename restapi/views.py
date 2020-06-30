# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer


class Get_Students(APIView):

    def get(self, request):

        try:
            limit = request.GET.get('limit')
            offset = request.GET.get('offset')

            res = StudentSerializer(Student.objects.all(), many=True).data

            if limit and offset:
                res = res[int(offset):int(limit) + int(offset)]
            if limit and not offset:
                res = res[0:int(limit)]
            if offset and not limit:
                res = res[int(offset):]

            if len(res) == 0:
                return Response({"status": "failure"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"results": res}, status=status.HTTP_200_OK)

        except Exception as e:
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=500)


class Get_Filtered_Students(APIView):

    def get(self, request):

        try:
            limit = request.GET.get('limit')
            offset = request.GET.get('offset')
            student_name_starts_with = request.GET.get('student_name_starts_with')

            res = StudentSerializer(Student.objects.filter(name__startswith=student_name_starts_with), many=True).data

            if limit and offset:
                res = res[int(offset):int(limit) + int(offset)]
            if limit and not offset:
                res = res[0:int(limit)]
            if offset and not limit:
                res = res[int(offset):]

            if len(res) == 0:
                return Response({"status": "failure"}, status=status.HTTP_404_NOT_FOUND)

            return Response({"results": res}, status=status.HTTP_200_OK)

        except Exception as e:
            error = {"status": "failure", "reason": str(e)}
            return JsonResponse(error, status=500)
