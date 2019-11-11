from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('api-token-auth', obtain_auth_token, name='api_token_auth'),
    path('create', views.create_broad_topic, name='create_broad_topic'),
    path('delete', views.delete_broad_topic, name='delete_broad_topic'),
    path('create-subtopic', views.create_subtopic, name='create-subtopic'),
    path('create-item', views.create_item, name='create-item'),
    path('delete-subtopic', views.delete_subtopic, name='delete-subtopic'),
    path('delete-item', views.delete_item, name='delete-item'),
    path('update-item', views.update_item, name='update-item'),
    path('update-subtopic', views.update_subtopic, name='update-subtopic'),
    path('update-topic', views.update_broad_topic, name='update-broad-topic'),
    path('update-item-priorities', views.update_item_priorities, name='update-item-priorities'),
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout')
]