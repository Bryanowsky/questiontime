from django.urls import include, path
from rest_framework.routers import DefaultRouter

from questions.api import views as questions_views

router = DefaultRouter()
router.register(r'questions', questions_views.QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('questions/<slug:slug>/answers/', questions_views.AnswerListAPIView.as_view(), name='answer-list'),
    path('questions/<slug:slug>/answer/', questions_views.AnswerCreateAPIView.as_view(), name='answer-create'),
    path('answers/<int:pk>/', questions_views.AnswerRetrieveUpdateDestroyAPIView.as_view(), name='answer-detail'),
    path('answers/<int:pk>/like/', questions_views.AnswerLikeAPIView.as_view(), name='answer-like')
]
