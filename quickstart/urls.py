
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article',ArticleViewSet, basename= 'article')

urlpatterns = [
    # path('',article_list),
    # path('<int:pk>',article_detail),

    # path('',ArticleView.as_view()),
    # path('<int:id>',ArticleDetail.as_view())

    # path('',GenericAPIView.as_view()),
    # path('<int:pk>',GenericDetailAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
   
]