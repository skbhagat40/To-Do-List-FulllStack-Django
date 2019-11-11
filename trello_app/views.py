from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import BroadTopicsSerializer
from .models import BroadTopics, SubTopics, Items
import json


@api_view(['GET'])
def home_view(request):
    serialized_data = BroadTopicsSerializer(BroadTopics.objects.filter(user=request.user), many=True)
    return Response({'data': serialized_data.data})


@api_view(['POST'])
def create_broad_topic(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    BroadTopics.objects.create(title=body.get('title'), user=request.user)
    return Response({'data': 'Topic Created Successfully!'})


@api_view(['POST'])
def delete_broad_topic(request):
    print('post request', request.body)
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    BroadTopics.objects.get(id=body.get('id'), user=request.user).delete()
    return Response({'data': 'Topic Deleted Successfully!'})


@api_view(['POST'])
def create_subtopic(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    subtopic = SubTopics.objects.create(title=body.get('title'))
    broad_topic = BroadTopics.objects.get(id=body.get('id'))
    subtopic.broadTopic = broad_topic
    subtopic.save()
    return Response({'data': 'Subtopic Created Successfully!'})


@api_view(['POST'])
def create_item(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    item = Items.objects.create(description=body.get('title'))
    subTopic = SubTopics.objects.get(id=body.get('id'))
    item.subTopic = subTopic
    item.save()
    return Response({'data': 'Item Created Successfully!'})


@api_view(['POST'])
def delete_subtopic(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    SubTopics.objects.get(id=body.get('id')).delete()
    return Response({'data': 'Subtopic Deleted Successfully'})


@api_view(['POST'])
def delete_item(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    Items.objects.get(id=body.get('id')).delete()
    return Response({'data': 'Item Deleted Successfully'})


@api_view(['PUT'])
def update_item(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    Items.objects.filter(id=body.get('id')).update(description=body.get('description'), status=body.get('status'))
    return Response({'data': 'Item Updated Successfully'})


@api_view(['PUT'])
def update_subtopic(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    SubTopics.objects.filter(id=body.get('id')).update(title=body.get('title'), status=body.get('status'))
    return Response({'data': 'Item Updated Successfully'})


@api_view(['PUT'])
def update_broad_topic(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    BroadTopics.objects.filter(id=body.get('id')).update(title=body.get('title'), status=body.get('status'))
    return Response({'data': 'Broad Topic Updated Successfully'})


@api_view(['POST'])
def update_item_priorities(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    items_list = body.get('items')
    for idx, val in enumerate(items_list):
        Items.objects.filter(id=val.get('id')).update(priority=idx)
    return Response({'data': 'Priorities Update Successfully'})


@csrf_exempt
def register(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    user_info = body.get('user_info')
    user = User.objects.create_user(username=user_info.get('username'), password=user_info.get('password'))
    user.save()
    login(request, user)
    return JsonResponse({'data': 'Logged In Successfully'})


@csrf_exempt
def login_user(request):
    if request.body is bytes:
        body_unicode = request.body.decode('utf-8')
    else:
        body_unicode = request.body
    body = json.loads(body_unicode)
    user_info = body.get('user_info')
    user = authenticate(request, username=user_info.get('username'), password=user_info.get('password'))
    if user is not None:
        login(request, user)
        return JsonResponse({'data': 'Logged in Successfully!!'})
    else:
        return JsonResponse({'error': 'Unable to Log In'}, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET'])
def logout_view(request):
    request.user.auth_token.delete()
    return Response({'data': 'Logged Out Successfully'}, status=status.HTTP_200_OK)
