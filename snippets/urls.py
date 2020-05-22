from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),
    path('users/', UserList.as_view()),
	path('users/<int:pk>/',UserDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)