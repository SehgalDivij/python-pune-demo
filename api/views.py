from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(http_method_names=['GET'])
def identify(request):
    """
    Simple view to return my name
    """
    return Response(data={'name': 'Divij Sehgal', 'occupation': 'Programming', 'reason': 'It\'s fun', 'age':22}, status=200)

