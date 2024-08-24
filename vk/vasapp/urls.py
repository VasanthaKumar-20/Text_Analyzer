from django.urls import path
from .views import SentimentAnalyzer

urlpatterns = [
    path('', SentimentAnalyzer.as_view(), name='analyze-sentiment'),
]
