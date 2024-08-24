from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from textblob import TextBlob

class SentimentAnalyzer(APIView):
    def post(self, request):
        text = request.data.get('text', '')
        if not text:
            return Response({"error": "No text provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        if sentiment > 0:
            sentiment_label = "Positive"
        elif sentiment < 0:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        return Response({"sentiment": sentiment_label, "polarity": sentiment}, status=status.HTTP_200_OK)
