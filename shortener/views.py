from django.shortcuts import redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import URL

@api_view(['POST'])
def shorten_url(request):
    original_url = request.data.get('original_url')
    if not original_url:
        return Response(
            {'error': 'original_url is required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    url = URL.objects.create(original_url=original_url)
    short_url = request.build_absolute_uri(f'/s/{url.short_code}/')
    return Response({
        'original_url': original_url,
        'short_url': short_url,
        'short_code': url.short_code
    }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def url_list(request):
    urls = URL.objects.all().order_by('-created_at')
    data = [
        {
            'id': url.id,
            'original_url': url.original_url,
            'short_code': url.short_code,
            'created_at': url.created_at
        }
        for url in urls
    ]
    return Response(data)

def redirect_url(request, short_code):
    try:
        url = URL.objects.get(short_code=short_code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return redirect('/')