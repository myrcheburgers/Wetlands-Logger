from msilib.schema import Patch
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from wetland_logger.models import User, Project, Datapoint
from wetland_logger.serializers import UserSerializer, UserPublicSerializer, ProjectSerializer, DatapointSerializer

from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_serializer = UserPublicSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET', 'PUT', 'PATCH'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return JsonResponse({'message':'Invalid user ID'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        user_serializer = UserPublicSerializer(user)
        return JsonResponse(user_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(data=user_serializer.data)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(data=project_serializer.data)
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH'])
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return JsonResponse({'message':'Invalid project ID'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        project_serializer = ProjectSerializer(project)
        return JsonResponse(project_serializer.data)
    elif request.method == 'PUT' or request.method == 'PATCH':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(project, data=project_data, partial=True)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse(data=project_serializer.data)
        return JsonResponse(project_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','POST'])
# @api_view(['GET'])
# def datapoint_list(request):
#     if request.method == 'GET':
#         datapoints = Datapoint.objects.all()
#         datapoints_serializer = DatapointSerializer(datapoints, many=True)
#         return JsonResponse(datapoints_serializer.data, safe=False)
    # elif request.method == 'POST':
    #     datapoint_data = JSONParser().parse(request)
    #     datapoint_serializer = DatapointSerializer(data=datapoint_data)
    #     if datapoint_serializer.is_valid():
    #         datapoint_serializer.save()
    #         return JsonResponse(data=datapoint_serializer.data)
    #     return JsonResponse(datapoint_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','POST'])
# def datapoint_detail(request, pk, fk):
def datapoint_list(request, fk):
    try:
        project = Project.objects.get(pk=fk)
    except Project.DoesNotExist:
        return JsonResponse({'message':'Invalid project ID'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        #TODO
        return None
    elif request.method == 'POST':
        datapoint_data = JSONParser().parse(request)
        datapoint_data['project_id'] = fk
        datapoint_serializer = DatapointSerializer(data=datapoint_data)
        # datapoint_serializer.set_project(fk)
        if datapoint_serializer.is_valid():
            datapoint_serializer.save()
            return JsonResponse(data=datapoint_serializer.data)
        return JsonResponse(datapoint_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class index(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/index.html'

#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})


# class list_all_tutorials(APIView):
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'tutorials/tutorial_list.html'

#     def get(self, request):
#         queryset = Tutorial.objects.all()
#         return Response({'tutorials': queryset})