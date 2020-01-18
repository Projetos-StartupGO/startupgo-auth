from django.conf import settings
from django.http import JsonResponse


def get_public_key(request):
    return JsonResponse(settings.JWT_PUBLIC_KEY)
